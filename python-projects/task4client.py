#chat application[client]
import socket
import threading

SERVER_HOST = '192.168.60.205'
SERVER_PORT = 12341

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(data)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

print("Type your message, or type 'exit' to leave the chat.")

while True:
    message = input()
    if message.lower() == 'exit':
        client_socket.send(message.encode('utf-8'))
        break
    elif message.strip():
        client_socket.send(message.encode('utf-8'))

client_socket.close()

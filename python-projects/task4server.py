#chat application[server]
import socket
import threading


SERVER_HOST = '0.0.0.0'
SERVER_PORT = 12341


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)


clients = []

def handle_client(client_socket, addr):

    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f'{addr[0]}:{addr[1]} - {data}')

            for client in clients:
                if client != client_socket:
                    client.send(data.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            break


    clients.remove(client_socket)
    client_socket.close()

print("Server is listening on {}:{}".format(SERVER_HOST, SERVER_PORT))

while True:
    client_socket, client_addr = server_socket.accept()
    clients.append(client_socket)
    print(f"Accepted connection from {client_addr[0]}:{client_addr[1]}")

    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_addr))
    client_handler.start()

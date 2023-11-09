import random
import string

def generate_password(length, num_letters, num_numbers, num_symbols):
    if length < num_letters + num_numbers + num_symbols:
        print("The sum of letter, number, and symbol counts exceeds the password length.")
        return

    # Initialize character sets
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    # Ensure there are enough characters in each set to meet the specified counts
    if len(letters) < num_letters or len(numbers) < num_numbers or len(symbols) < num_symbols:
        print("Invalid character counts. Please choose smaller counts.")
        return

    # Generate each character type separately
    password = ''.join(random.choice(letters) for _ in range(num_letters))
    password += ''.join(random.choice(numbers) for _ in range(num_numbers))
    password += ''.join(random.choice(symbols) for _ in range(num_symbols))

    # Fill the remaining length with random characters from all character sets
    remaining_length = length - (num_letters + num_numbers + num_symbols)
    characters = letters + numbers + symbols
    password += ''.join(random.choice(characters) for _ in range(remaining_length))

    # Shuffle the password to randomize the order
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def main():
    length = int(input("Enter the password length: "))
    num_letters = int(input("Enter the number of letters: "))
    num_numbers = int(input("Enter the number of numbers: "))
    num_symbols = int(input("Enter the number of symbols: "))

    password = generate_password(length, num_letters, num_numbers, num_symbols)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()

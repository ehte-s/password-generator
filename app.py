import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password):
    with open('passwords.txt', 'a') as file:
        file.write(password + '\n')
    print(f"Password '{password}' has been saved to passwords.txt")

def generate_and_save_password(length=12):
    password = generate_password(length)
    save_password(password)
    return password

if __name__ == "__main__":
    new_password = generate_and_save_password()
    print(f"Generated password: {new_password}")


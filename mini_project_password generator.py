import random
import string

characters = list(string.ascii_letters + string.digits + "$%^&%*()@")


def generate_password():
    password_length = int(input("Length of password: "))

    random.shuffle(characters)  # shuffle the characters

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)  # make it more random

    password = "".join(password)

    print(f"\nYour new password: {password}")


while True:
    command = input("\nCreate a password - yes or no: ")
    if command.lower() == "no":
        print("Program ended")
        break

    else:
        generate_password()

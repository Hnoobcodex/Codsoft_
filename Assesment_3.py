import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a valid positive length.")
            return
    except ValueError:
        print("Please enter a valid number for the length.")
        return

    generated_password = generate_password(length)
    
    print(f"\nGenerated Password: {generated_password}")

if __name__ == "__main__":
    main()

# MJT

def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    while True:
        print("\n*** Caesar Cipher ***")
        print(" 1. Encrypt Message")
        print(" 2. Decrypt Message")
        print(" 3. Exit program")
        choice = input("Select Number: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 3:
            print("Exiting the program.")
            break
        elif choice in [1, 2]:
            text = input("Enter your message: ")
            shift = int(input("Enter shift value: "))

            if choice == 1:
                encrypted_text = encrypt(text, shift)
                print(f"Encrypted Text: '{encrypted_text}'")
            elif choice == 2:
                decrypted_text = decrypt(text, shift)
                print(f"Decrypted Text: '{decrypted_text}'")
        else:
            print("\nInvalid choice. Please choose '1' for encryption, '2' for decryption, or '3' to exit program.")


if __name__ == "__main__":
    main()


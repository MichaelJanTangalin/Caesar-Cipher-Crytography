# Michael Jan R. Tangalin
# Task # 1: Implement Caesar Cipher (GUI Version)


import tkinter as tk
from tkinter import messagebox


# Caesar Cipher functions
def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# GUI application
class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher Program")

        self.label = tk.Label(root, text="Caesar Cipher Cryptography", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.text_label = tk.Label(root, text="Enter your message:")
        self.text_label.pack()
        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack(pady=5)

        self.shift_label = tk.Label(root, text="Enter shift value:")
        self.shift_label.pack()
        self.shift_entry = tk.Entry(root, width=5, justify='center')
        self.shift_entry.pack(pady=5)

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_message)
        self.encrypt_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_message)
        self.decrypt_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.pack()
        self.result_text = tk.Text(root, height=5, width=50)
        self.result_text.pack(pady=10)

    def encrypt_message(self):
        text = self.text_entry.get()
        shift = self.shift_entry.get()
        if not shift.isdigit():
            messagebox.showerror("Invalid Input", "Shift value must be an integer.")
            return
        shift = int(shift)
        encrypted_text = encrypt(text, shift)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, encrypted_text)

    def decrypt_message(self):
        text = self.text_entry.get()
        shift = self.shift_entry.get()
        if not shift.isdigit():
            messagebox.showerror("Invalid Input", "Shift value must be an integer.")
            return
        shift = int(shift)
        decrypted_text = decrypt(text, shift)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, decrypted_text)


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)  # Disable resizing in both directions
    app = CaesarCipherApp(root)
    root.mainloop()

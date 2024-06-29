import tkinter as tk
from tkinter import messagebox

def encrypt(text, s):
    result1 = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result1 += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result1 += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result1 += char
    return result1

def decrypt(c, s):
    result2 = ""
    for i in range(len(c)):
        char = c[i]
        if char.isupper():
            result2 += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result2 += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result2 += char
    return result2

def perform_encryption():
    text = text_entry.get()
    try:
        s = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer")
        return
    
    encrypted_text = encrypt(text, s)
    encrypted_text_var.set(encrypted_text)

def perform_decryption():
    text = text_entry.get()
    try:
        s = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer")
        return
    
    decrypted_text = decrypt(text, s)
    decrypted_text_var.set(decrypted_text)

# Set up the main window
root = tk.Tk()
root.title("Caesar Cipher GUI")

# Text Entry
tk.Label(root, text="Enter text:").grid(row=0, column=0, padx=10, pady=10)
text_entry = tk.Entry(root, width=50)
text_entry.grid(row=0, column=1, padx=10, pady=10)

# Shift Value Entry
tk.Label(root, text="Enter shift value:").grid(row=1, column=0, padx=10, pady=10)
shift_entry = tk.Entry(root, width=10)
shift_entry.grid(row=1, column=1, padx=10, pady=10)

# Encrypt Button
encrypt_button = tk.Button(root, text="Encrypt", command=perform_encryption)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

# Decrypt Button
decrypt_button = tk.Button(root, text="Decrypt", command=perform_decryption)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Encrypted Text Display
tk.Label(root, text="Encrypted text:").grid(row=3, column=0, padx=10, pady=10)
encrypted_text_var = tk.StringVar()
encrypted_text_display = tk.Entry(root, textvariable=encrypted_text_var, state='readonly', width=50)
encrypted_text_display.grid(row=3, column=1, padx=10, pady=10)

# Decrypted Text Display
tk.Label(root, text="Decrypted text:").grid(row=4, column=0, padx=10, pady=10)
decrypted_text_var = tk.StringVar()
decrypted_text_display = tk.Entry(root, textvariable=decrypted_text_var, state='readonly', width=50)
decrypted_text_display.grid(row=4, column=1, padx=10, pady=10)

# Run the application
root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Fungsi enkripsi menggunakan Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi dekripsi menggunakan Caesar Cipher
def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift - shift_amount) % 26 + shift_amount)
        else:
            decrypted_text += char
    return decrypted_text

# Fungsi untuk enkripsi ketika tombol ditekan
def encrypt_message():
    try:
        shift = int(entry_shift.get())
        message = entry_message.get()
        encrypted = caesar_encrypt(message, shift)
        result_label.config(text=f"Teks Terenkripsi: {encrypted}")
    except ValueError:
        messagebox.showerror("Masukan Tidak Valid", "Nilai shift harus berupa integer.")

# Fungsi untuk dekripsi ketika tombol ditekan
def decrypt_message():
    try:
        shift = int(entry_shift.get())
        message = entry_message.get()
        decrypted = caesar_decrypt(message, shift)
        result_label.config(text=f"Teks Didekripsi: {decrypted}")
    except ValueError:
        messagebox.showerror("Masukan Tidak Valid", "Nilai shift harus berupa integer.")

# Membuat GUI dengan Tkinter
root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")

tk.Label(root, text="pesan:").grid(row=0, column=0, padx=10, pady=10)
entry_message = tk.Entry(root, width=50)
entry_message.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="shift:").grid(row=1, column=0, padx=10, pady=10)
entry_shift = tk.Entry(root, width=5)
entry_shift.grid(row=1, column=1, padx=10, pady=10, sticky="w")

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

result_label = tk.Label(root, text="Hasilnya akan muncul di sini")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

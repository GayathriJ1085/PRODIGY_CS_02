import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


def encrypt_image(image, key):
    for i in range(0, len(image), 2):
        if i + 1 < len(image):
            image[i], image[i + 1] = image[i + 1], image[i]
            image[i] = (image[i] + key) % 256
            image[i + 1] = (image[i + 1] + key) % 256
    return image

# To open the path 
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

# Encryption
def handle_encryption():
    path = entry_path.get().strip()
    key_input = combo_key.get().strip()

    path = os.path.normpath(path)

    if not os.path.isfile(path):
        messagebox.showerror("Error", 'File not found, please check the path and try again.')
        return

    # Invalid number
    if not key_input.isdigit():
        messagebox.showerror("Error", 'Invalid key. Please enter an integer value for the key.')
        return

    key = int(key_input)

    if key < 0 or key > 255:
        messagebox.showerror("Error", 'Invalid key. Please enter a value between 0 and 255.')
        return

    print('The path of file:', path)
    print('Key for encryption:', key)

    if os.access(path, os.R_OK):
        try:
            with open(path, 'rb') as fin:
                image = fin.read()
        except Exception as e:
            messagebox.showerror("Error", f'Error reading the file: {e}')
            return
    else:
        messagebox.showerror("Error", 'The file cannot be read. Please check the file permissions and try again.')
        return

    image = bytearray(image)
    encrypted_image = encrypt_image(image, key)

    if os.access(path, os.W_OK):
        try:
            with open(path, 'wb') as fout:
                fout.write(encrypted_image)
        except Exception as e:
            messagebox.showerror("Error", f'Error writing to the file: {e}')
            return
    else:
        messagebox.showerror("Error", 'The file cannot be written. Please check the file permissions and try again.')
        return

    messagebox.showinfo("Success", "Encryption Done!")

# The window
root = tk.Tk()
root.title("Image Encryption")
root.configure(bg='green')

lab = tk.Label(root, text="Encrypt Image", font=('Arial Rounded MT Bold', 25), bg="green")
lab.grid(row=0, column=1, padx=10, pady=20)

# Image
label_path = tk.Label(root, text="Select Image File:", font=("ADLaM Display", 10, "bold"), bg="green")
label_path.grid(row=1, column=0, padx=10, pady=10)
entry_path = tk.Entry(root, width=50)
entry_path.grid(row=1, column=1, padx=10, pady=10)

button_browse = tk.Button(root, text="Browse", command=select_file, font=("ADLaM Display", 10, "bold"))
button_browse.grid(row=1, column=2, padx=10, pady=10)

label_key = tk.Label(root, text="Enter Key:", font=("ADLaM Display", 10, "bold"), bg="green")
label_key.grid(row=2, column=0, padx=10, pady=10)
combo_key = ttk.Combobox(root, width=47)
combo_key['values'] = [str(i) for i in range(256)] 
combo_key.grid(row=2, column=1, padx=10, pady=10)

button_encrypt = tk.Button(root, text="Encrypt", command=handle_encryption, bg="orange",font=('Arial',11,"bold"))
button_encrypt.grid(row=3, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()

import os
import tkinter as tk
from tkinter import filedialog, messagebox

# process of swapping pixel values 
def encrypt_image(image, key):
    for i in range(0, len(image), 2):
        if i + 1 < len(image):
            
            image[i], image[i + 1] = image[i + 1], image[i]
            
            image[i] = (image[i] + key) % 256
            image[i + 1] = (image[i + 1] + key) % 256
    return image

#to open the path 
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

#encryption
def handle_encryption():
    path = entry_path.get().strip()
    key_input = entry_key.get().strip()


    path = os.path.normpath(path)

    # if the path is not there
    if not os.path.isfile(path):
        messagebox.showerror("Error", f'The file "{path}" was not found. Please check the path and try again.')
        return

    # invalid number
    if not key_input.isdigit():
        messagebox.showerror("Error", 'Invalid key. Please enter an integer value for the key.')
        return

    key = int(key_input)

    print('The path of file:', path)
    print('Key for encryption:', key)

    if os.access(path, os.R_OK):
        with open(path, 'rb') as fin:
            # Storing image data in variable "image"
            image = fin.read()
    else:
        messagebox.showerror("Error", 'The file cannot be read. Please check the file permissions and try again.')
        return


    image = bytearray(image)

    image = encrypt_image(image, key)

    if os.access(path, os.W_OK):
        with open(path, 'wb') as fout:
            fout.write(image)
    else:
        messagebox.showerror("Error", 'The file cannot be written. Please check the file permissions and try again.')
        return

    messagebox.showinfo("Success", "Encryption Done!")

# the window
root = tk.Tk()
root.title("Image Encryption")

#image
label_path = tk.Label(root, text="Select Image File:")
label_path.grid(row=0, column=0, padx=10, pady=10)
entry_path = tk.Entry(root, width=50)
entry_path.grid(row=0, column=1, padx=10, pady=10)


button_browse = tk.Button(root, text="Browse", command=select_file)
button_browse.grid(row=0, column=2, padx=10, pady=10)

label_key = tk.Label(root, text="Enter Encryption Key:")
label_key.grid(row=1, column=0, padx=10, pady=10)

entry_key = tk.Entry(root, width=50)
entry_key.grid(row=1, column=1, padx=10, pady=10)

button_encrypt = tk.Button(root, text="Encrypt", command=handle_encryption)
button_encrypt.grid(row=2, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
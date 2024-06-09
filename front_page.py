import tkinter as tk
import subprocess

def open_encryption_gui():
    subprocess.Popen(['python', 'TASK_02.py'])

def open_decryption_gui():
    subprocess.Popen(['python', 'task_2.py'])

# Window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("600x400")
root.configure(bg='black')

#alignments
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# introduction
lab1 = tk.Label(root, text="Pixel Manipulation", fg='white',bg="black", font=('Harlow Solid Italic', 30))
lab1.grid(row=0, column=1, pady=25)

lab2 = tk.Label(root, text="Welcome to 'Pixel Manipulation' ", fg='white',bg="black", font=('Elephant', 15))
lab2.grid(row=1, column=1, pady=25,sticky="s")

lab3 = tk.Label(root, text="Please click on 'Encryption' to hide your picture file \n and 'Decryption' to get it back",fg='white',bg="black", font=('Times New Roman', 15,'bold'))
lab3.grid(row=2, column=1, pady=25,sticky="n")

#encryption button
encryption_button = tk.Button(root, text="Encryption", command=open_encryption_gui)
encryption_button.grid(row=4, column=1, padx=4, pady=10,sticky="w")

#decryption button
decryption_button = tk.Button(root, text="Decryption", command=open_decryption_gui)
decryption_button.grid(row=4, column=1, padx=4, pady=10,sticky="e")

#ending
lab4 = tk.Label(root, text="Contact us incase you forget the 'key number' ",fg='white',bg="black", font=('Times New Roman', 11))
lab4.grid(row=5, column=1, pady=15,sticky="n")

lab4 = tk.Label(root, text="email id:gayathrij23@gmail.com ",fg='white',bg="black", font=('Times New Roman', 6))
lab4.grid(row=5, column=1,sticky="s")


root.mainloop()
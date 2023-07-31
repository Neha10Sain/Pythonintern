import tkinter as tk
import random
import string


def generate_password():
    name = name_entry.get()
    password_length = int(length_entry.get())
    if password_length <= 0:
        password_result.set("Password length must greater than 0")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for _ in range(password_length))

    # Concatenate user's name and the randomly generated password
    generated_password = name + "_" + random_password
    password_result.set(generated_password)

# Create the main application window
data = tk.Tk()
data.title("Password Generator")
data.geometry("400x300")

# Label and Entry for user's name input
name_label = tk.Label(data, text="Enter Your Name")
name_label.pack(pady=10)
name_entry = tk.Entry(data)
name_entry.pack(pady=5)

# Label and Entry for password length input
length_label = tk.Label(data, text="Enter Password Length")
length_label.pack(pady=10)
length_entry = tk.Entry(data)
length_entry.pack(pady=5)

# Button
generate_button = tk.Button(data, text="Generated Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display generated pass
password_result = tk.StringVar()
password_result_label = tk.Label(data, textvariable=password_result, wraplength=200)
password_result_label.pack(pady=10)

data.mainloop()

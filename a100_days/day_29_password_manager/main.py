from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website_name = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_name} exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_input.get()
    username = username_input.get()
    password = password_input.get()

    new_data = {
        website_name: {
            "email": username,
            "password": password
        }
    }

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving data & Create a new file
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

# Label website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# Input website
website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

# Button Search
search_button = Button(width=13, text="Search", command=find_password)
search_button.grid(row=1, column=2)

# Label username
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

# Input username
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "albert@email.com")

# Label password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Input password
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Button Generate
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

# Button Add
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

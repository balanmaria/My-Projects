from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ------------------------------- FIND PASSWORD --------------------------------- #

def find_password():
    try:
        with open("data.json", "r") as file:
            # Reading old data
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Ooops", message="No Data File Found!")

    else:
        if input_web.get() in data:
            messagebox.showinfo(title=f"{input_web.get()}'s Information",
                                message=f'Email: {data[input_web.get()]["email"]}\nPassword: {data[input_web.get()]["password"]}')
        else:
            messagebox.showinfo(title=f"Error",
                                message=f"No details for the {input_web.get()} website exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = [random.choice(letters) for _ in range(1, random.randint(8, 10) + 1)]
    password += [random.choice(symbols) for _ in range(1, random.randint(2, 4) + 1)]
    password += [random.choice(numbers) for _ in range(1, random.randint(2, 4) + 1)]
    random.shuffle(password)

    # mypass=""
    # for i in password:
    #     mypass += i
    mypass = "".join(password)
    input_password.insert(0, mypass)
    pyperclip.copy(mypass)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():
    # my_text=input_web.get() + " | " + input_email.get() + " | " + input_password.get() + "\n"
    my_text = f"{input_web.get()} | {input_email.get()} | {input_password.get()} \n"
    new_data = {
        input_web.get(): {
            "email": input_email.get(),
            "password": input_password.get()
        }}

    if len(input_password.get()) != 0 and len(input_email.get()) != 0 and len(input_web.get()) != 0:
        # Create a message box
        is_ok = messagebox.askokcancel(title=input_web.get(),
                                       message=f"These are the details entered: \nEmail: {input_email.get()}\nPassword: {input_password.get()}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # Reading old data
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    # Saving update data
                    json.dump(new_data, file, indent=4)

            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as file:
                    # Saving update data
                    json.dump(data, file, indent=4)

            finally:
                # input_email.delete(0, END)
                input_password.delete(0, END)
                input_web.delete(0, END)
    else:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

canvans = Canvas(width=200, height=200, highlightthickness=0)
imagine = PhotoImage(file="logo.png")
canvans.create_image(100, 100, image=imagine)
canvans.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
input_web = Entry(width=26)
input_web.grid(column=1, row=1)
input_web.focus()
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
input_email = Entry(width=46)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "maria@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
input_password = Entry(width=26)
input_password.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45, command=add_pass)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

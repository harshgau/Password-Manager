from tkinter import *
from tkinter import messagebox
import random



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

    password_letters = []
    password_symbols = []
    password_numbers = []

    password_letters = [random.choice(letters) for value in range(nr_letters)]
    password_symbols = [random.choice(symbols) for value in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for value in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    text_password.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = text_website.get()
    email = text_email.get()
    password = text_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave field empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                                                              f"\npassword:{password}\nIs it ok to Save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} |  {password}\n")
            text_website.delete(0, END)
            text_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
text_website = Entry(width=43)
text_website.grid(row=1, column=1, columnspan=2)
text_website.focus()
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)
text_email = Entry(width=43)
text_email.grid(row=2, column=1, columnspan=2)
text_email.insert(0, "harshgautam499@gmail.com")
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)
text_password = Entry(width=25)
text_password.grid(row=3, column=1)
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()

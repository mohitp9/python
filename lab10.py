from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu, Spinbox
import re

def validate_input(input_text, regex):
    return re.match(regex, input_text) is not None

name_regex = r"^[A-Za-z\s]+$"
email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
phone_regex = r"^\d{10}$"

root = Tk()
root.title("Domain Form")

name_label = Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

email_label = Label(root, text="Email:")
email_label.grid(row=1, column=0)
email_entry = Entry(root)
email_entry.grid(row=1, column=1)

phone_label = Label(root, text="Phone Number:")
phone_label.grid(row=2, column=0)
phone_entry = Entry(root)
phone_entry.grid(row=2, column=1)

gender_label = Label(root, text="Gender:")
gender_label.grid(row=3, column=0)
gender_var = StringVar(root)
gender_var.set("Male")
gender_option = OptionMenu(root, gender_var, "Male", "Female")
gender_option.grid(row=3, column=1)

year_label = Label(root, text="Year/DoB:")
year_label.grid(row=4, column=0)
year_spinbox = Spinbox(root, from_=1900, to=2023)
year_spinbox.grid(row=4, column=1)

def validate_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if not validate_input(name, name_regex):
        error_label.config(text="Invalid Name", fg="red")
    elif not validate_input(email, email_regex):
        error_label.config(text="Invalid Email", fg="red")
    elif not validate_input(phone, phone_regex):
        error_label.config(text="Invalid Phone Number", fg="red")
    else:
        error_label.config(text="Form submitted successfully", fg="green")

submit_button = Button(root, text="Submit", command=validate_form)
submit_button.grid(row=5, column=0, columnspan=2)

error_label = Label(root, text="")
error_label.grid(row=6, column=0, columnspan=2)

root.mainloop()
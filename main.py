from tkinter import *
from tkinter import messagebox
import json

from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    Password_entry.insert(0, password)
    pyperclip.copy(password)



def save_info():
        website = website_entry.get()
        email=Email_entry.get()
        password=Password_entry.get()
        new_data= {
            website: {"email": email,
        "password": password, }
        }

        if len(website)==0 or len(password)==0:
            messagebox.showinfo(title="Oops",message="Please input information")
        else:
            try:
                with open("data.json","r") as data_file:
                       # json.dump(new_data, data_file ,indent=4) #data_file is the location where we want to dump json file
                        #reading old data
                        data=json.load(data_file)
                       # print(data) #this takes json data and converts it into python dict
                       #updating old data with new data
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)



                   #now we have to write the updated data back into data file

            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                #saving updated data
            finally:
                website_entry.delete(0,END)
                Password_entry.delete(0,END)


def search_button():
    website=website_entry.get()
    try:
        with open ("data.json") as data_file:
            data=json.load(data_file) #parse a valid JSON string and convert it into a Python Dictionary
        #print(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File does not exist")
    else:
        if website in data:
            email= data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message= f"email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Website not found",message=f"{website} does not exist")


# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(width=200, height=200)
canvas.grid(row=0,column=1)
logo_png=PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=logo_png)

website_label=Label(text="Website :")
website_label.grid(row=1,column=0)
website_entry=Entry(width=25)
website_entry.grid(row=1,column=1)
website_entry.focus()


Email_username=Label(text="Email/username :")
Email_username.grid(row=2,column=0)
Email_entry=Entry(width=25)
Email_entry.grid(row=2,column=1)
Email_entry.insert(0,"")

Password=Label(text="Password :")
Password.grid(row=3,column=0)
Password_entry=Entry(width=25)
Password_entry.grid(row=3,column=1)


generate_button=Button(text="generate password",command=generate_password)
generate_button.grid(row=3,column=2)

search_button= Button(text="Search",command=search_button)
search_button.grid(row=1,column=2,columnspan=2)

add_button=Button(text="Add",width=35,command=save_info)
add_button.grid(row=4,column=1,columnspan=2)





window.mainloop()
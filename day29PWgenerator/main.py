from tkinter import *
from tkinter import messagebox
from random_pw_generator import generate_pw
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def add_new_pw():
    new_pw = generate_pw()
    pw_entry.insert(0, new_pw)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pw():
    website = website_entry.get()
    email = email_entry.get()
    pw = pw_entry.get()
    if len(website) ==0 or len(pw) ==0:
        messagebox.showinfo(title = "error", message="ensure no blanks")
    else:
        entry = {website:
                     {"email": email,
                      "password": pw,
                     }
                 }
        try:
            with open('pw_manager.json', "r") as f:
                #read old file
                data = json.load(f)
        except FileNotFoundError:
            with open('pw_manager.json', "w") as f:
                json.dump(entry, f, indent= 4)
        else: #update the json file
            data.update(entry)
            with open('pw_manager.json', "w") as f:
                #write it back
                json.dump(data, f,indent = 4 )

        finally:

                website_entry.delete(0, END)
                pw_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx = 20, pady = 20, bg = "white")
canvas = Canvas(width = 200, height=200, highlightthickness= 0, bg= "white")
mypass = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = mypass)
canvas.grid(row = 0, column =1)
#website
#Labels
website_label = Label(text="Website:", fg = "black", bg = "white")
website_label.grid(row = 1, column=0)
#Entries
website_entry = Entry(width=21)
website_entry.focus()

website_entry.grid(row = 1, column =1)
#Email
#Labels
email_label = Label(text="Email/Username:", fg = "black", bg = "white")
email_label.grid(row = 2, column=0)
#Entries
email_entry = Entry(width=35)
#Add some text to begin with
email_entry.insert(0, string = "carrie.kan@hanmail.com")
#Gets text in entry
print(email_entry.get())
email_entry.grid(row = 2, column =1, columnspan=2)
#PW
#Labels
pw_label = Label(text="Password:", fg = "black", bg = "white")
pw_label.grid(row = 3, column=0)
#Entries
pw_entry = Entry(width=21)
#Add some text to begin with
pw_entry.insert(END, string = "")
#Gets text in entry
print(pw_entry.get())
pw_entry.grid(row = 3, column =1)
#Buttons

#calls action() when pressed
generate_button = Button(text="Generate Password", command=add_new_pw, width = 15)
generate_button.grid(row =3, column=2 )

#Add button

#Buttons


#calls action() when pressed
add_button = Button(text="Add", command=add_pw, width = 36)
add_button.grid(row =4, column=1, columnspan= 2)

def search_pw():
    website = website_entry.get()
    try:
        with open("pw_manager.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Not found", message="no data file found")
    except ValueError:
        messagebox.showinfo(title="Not found", message="no data file found")
    else:
        if website in data:
            dict_website = data[website]
            email = dict_website["email"]
            password = dict_website["password"]
            messagebox.showinfo(title="found", message=f"email:{email} \nPW:{password}")
        else:
            messagebox.showinfo(title="Not found", message="no data file found")

search_button = Button(text = "Search", command = search_pw, width = 15)
search_button.grid(row =1, column=2)

window.mainloop()
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import mysql.connector
import json
import os
import re


# Password Generator

def passwordGenerator():
    lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z']
    upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&',
               '(', ')', '*', '+', '=', ':', ';', '?', '>', '<']

    lettersList1 = [random.choice(lowerCase) for _ in range(5)]
    lettersList2 = [random.choice(upperCase) for _ in range(5)]
    numbersList = [random.choice(numbers) for _ in range(3)]
    symbolList = [random.choice(symbols) for _ in range(3)]
    passwordList = lettersList1 + lettersList2 + numbersList + symbolList
    random.shuffle(passwordList)
    password = "".join(passwordList)
    passwordEntry.insert(0, password)
    pyperclip.copy(password)


# -------------------------------------------------------------------------------------------------------------------
# Stoing data in the database

def storedata():

    appName = websiteURLEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()

    if len(appName) == 0 or len(password) == 0:
        messagebox.showinfo(
            message="Please make sure that each and every field is filled up")

    with open('config.json') as json_file:
        data = json.load(json_file)
    print()

    mydb = mysql.connector.connect(
        host=data["host"],
        user=data["user"],
        password=data["passwd"],
        database="lockerdb"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO locker (website, mail, password) VALUES (%s, %s,%s)"
    val = (appName, email, password)

    mycursor.execute(sql, val)

    mydb.commit()

    websiteURLEntry.delete(0, 'end')
    emailEntry.delete(0, 'end')
    passwordEntry.delete(0, 'end')

# -------------------------------------------------------------------------------------------------------------------
# Searching passwords


def search():
    appName = websiteURLEntry.get()
    email = emailEntry.get()

    if len(appName) == 0 or len(email) == 0:
        messagebox.showinfo(
            message="Please make sure that each and every field is filled up")

    with open('config.json') as json_file:
        data = json.load(json_file)
    print()

    mydb = mysql.connector.connect(
        host=data["host"],
        user=data["user"],
        password=data["passwd"],
        database="lockerdb"
    )

    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT password FROM locker WHERE mail = %s AND website = %s", (email, appName))

    myresult = mycursor.fetchone()
    myresult = myresult[0]
    pyperclip.copy(myresult)
    messagebox.showinfo(message="Password copied")


# -------------------------------------------------------------------------------------------------------------------
# Deleting passwords

def delete():

    appName = websiteURLEntry.get()
    email = emailEntry.get()

    with open('config.json') as json_file:
        data = json.load(json_file)
    print()

    mydb = mysql.connector.connect(
        host=data["host"],
        user=data["user"],
        password=data["passwd"],
        database="lockerdb"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM locker WHERE website=%s AND mail=%s"
    adr = (appName, email)

    mycursor.execute(sql, adr)

    mydb.commit()

    # mycursor.execute("SET SQL_SAFE_UPDATES = 0;")
    # mycursor.execute("DELETE row FROM locker WHERE website=%s AND mail=%s", (appName, email))

    messagebox.showinfo(message="Your password has been successfully deleted")


# -------------------------------------------------------------------------------------------------------------------
# Frontend
window = Tk()
window.title("Locker")
window.config(padx=200, pady=100)
window.configure(background='#172b3f')

# Window
canvas = Canvas(height=200, width=200, highlightthickness=0)
logo = PhotoImage(file="locker logo.png")
canvas.create_image(100, 130, image=logo)
canvas.grid(row=0, column=1)

# Input Info
websiteURL = Label(text="Website: ", background='#172b3f',
                   foreground='#42c1b6')
websiteURL.grid(row=1, column=0)
email = Label(text="Email: ", background='#172b3f', foreground='#42c1b6')
email.grid(row=2, column=0)
password = Label(text="Password: ", background='#172b3f', foreground='#42c1b6')
password.grid(row=3, column=0)

# Info Entry Feild
websiteURLEntry = Entry(width=53)
websiteURLEntry.grid(row=1, column=1, columnspan=2, pady=5)
websiteURLEntry.focus()
emailEntry = Entry(width=53)
emailEntry.grid(row=2, column=1, columnspan=2, pady=5)
passwordEntry = Entry(width=34)
passwordEntry.grid(row=3, column=1, pady=5)

# Buttons
generatePassword = Button(text="Generate", width=14, command=passwordGenerator,
                          background='#42c1b6', foreground='#172b3f', highlightthickness=0, bd=0)
generatePassword.grid(row=3, column=2, padx=3)
add = Button(text="Add", width=29, command=storedata, background='#42c1b6',
             foreground='#172b3f', highlightthickness=0, bd=0)
add.grid(row=4, column=1, pady=5)
search = Button(text="Search", width=14, command=search,
                background='#42c1b6', foreground='#172b3f', highlightthickness=0, bd=0)
search.grid(row=4, column=2)
delete = Button(text="Delete", width=29, command=delete,
                background='#42c1b6', foreground='#172b3f', highlightthickness=0, bd=0)
delete.grid(row=5, column=1)
window.mainloop()

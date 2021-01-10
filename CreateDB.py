from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import mysql.connector
import json
import os

# Creating database

with open('config.json') as json_file:
    data = json.load(json_file)
print()

mydb = mysql.connector.connect(
host=data["host"],
user=data["user"],
password=data["passwd"]
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE lockerdb")

mydb = mysql.connector.connect(
host=data["host"],
user=data["user"],
password=data["passwd"],
database="lockerdb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE locker (website VARCHAR(255), mail VARCHAR(255), password VARCHAR(255))")


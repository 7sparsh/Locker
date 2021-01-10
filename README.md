# Locker
Locker is a Python &amp; MySQL powered password manager. 

# Installation
## Dependencies
MySQL Server, MySQL connector and pyperclip

MySQL Server can be installed by visiting https://dev.mysql.com/downloads/mysql/

The rest can be installed through pip: i.e. pip install pyperclip

This program is written in Python3.

## Setup

You must have the following installed:

-	MySQL Server 
-	MySQL Connector
-	Python3

After setting up your MySQL Server, load up config.json and change the file to match your credentials as follows:

  {
  
    "host": "host",
    "user": "username",
    "passwd": "password"
    
  }
  
Then save and run createDB.py to create the database and table. This file needs to be run just once.

Finally run the frontend.py file to store and manipulate data in the database.
## Usage
This application can be used to store various details of the user which are concerned with websites, emails and passwords. As example – bank details, different account details etc.

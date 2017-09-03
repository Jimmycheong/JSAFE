# Jsafe - A free & secure way of storing passwords. 
![screen shot 2016-12-30 at 16 20 01](https://cloud.githubusercontent.com/assets/22529514/21568373/da507322-ceab-11e6-9eb6-b46550c5d14e.jpg) 
Writing my third app! 
- Written in Python3 
- Tkinter Module for GUI development 
- Time taken to build verson 1.0: 2 days 
- Requires installation of following modules: pycryptography, sqlalchemy, pillow
- Encrypted passwords stored on SQLite database.

# Setup 

1. Install dependancies via pip and brew. 
2. Open the terminal and go into the directory. 
3. Create a sqlite3 database file by typing ``python jdb.py``
4. Create a new password by typing``python reset_password.py``
5. Run the application by typing ``python jsafe.py``

## Initial authentication screen: 
![screen shot 2016-12-30 at 16 19 18](https://cloud.githubusercontent.com/assets/22529514/21568384/ed7b1510-ceab-11e6-9946-1d564cfccb4c.jpg) 

- Uses SHA256 hashing algorithm for authenication and key for password encryption.

## What I learnt from this project: 
- Fundamental value of unicode, along with the .encode() and decode() functions
- How to write encryption functions using methods from the pycryptography module 
- How to build treeviews using TKinter GUI tools 

## Future Tasks: 
- Improve GUI interface 
- Allow user to set their own password hash through the initial screen.

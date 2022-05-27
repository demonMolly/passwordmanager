import sqlite3, hashlib
from tkinter import *

window = Tk()
window.title("Password Manager")

def loginScreen():
    window.geometry("350x150")
    
    lbl = label(window, text="Enter the password")
    lbl.config(anchor=CENTER)
    lbl.pack()

loginScreen()
window.mainloop()

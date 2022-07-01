from tkinter import messagebox
from tkinter import *


Gmail = input("Enter Your Email-ID:").strip()

UserName = Gmail[:Gmail.index('@')]
Domain = Gmail[Gmail.index('@')+1:]

print(f"Your Username is {UserName} & Your Domain Name is {Domain}")


messagebox.showinfo("Information", f"Your Username is {UserName} & Your Domain Name is {Domain}")
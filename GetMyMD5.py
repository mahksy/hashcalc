from tkinter import *
import customtkinter
import sys
import hashlib

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
customtkinter.deactivate_automatic_dpi_awareness()

root = customtkinter.CTk()
root.title("Hash calculator")
root.geometry('400x150')
root.grid_columnconfigure(1, weight=1)

def gethash():
    tohash=myinput.get()
    hashed=hashlib.md5(tohash.encode('utf-8')).hexdigest()
    myresult.configure(state="normal")
    myresult.delete("1.0","end")
    myresult.insert("0.0", str(hashed))
    myresult.configure(state="disabled")    


inputlabel = customtkinter.CTkLabel(root, text="Data to hash: ")
inputlabel.grid(row=1, column=0, padx=10, pady=10)

myinput = customtkinter.CTkEntry(root, placeholder_text=(""))
myinput.grid(row=1, column =1, padx=10, pady=10, sticky="ew")

mybutton = customtkinter.CTkButton(root, text='Calculate MD5 Hash', command=gethash)
mybutton.grid(columnspan=2,row=2, column= 0, padx = 10, pady= 10, sticky ="ew")

outputlabel = customtkinter.CTkLabel(root, text="Result: ")
outputlabel.grid(row=3, column=0, padx=10, pady=10)

myresult = customtkinter.CTkTextbox(root, height=15)
myresult.grid(row=3, column=1, padx = 10, pady= 10, sticky ="ew")

root.mainloop()
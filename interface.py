from tkinter import *
import customtkinter
import sys
import hashlib

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
customtkinter.deactivate_automatic_dpi_awareness()


root = customtkinter.CTk()
root.title("Hash calculator")
root.geometry('300x200')
root.grid_columnconfigure(0, weight=1)

def gethash():
    tohash=myinput.get()
    hashed=hashlib.md5(tohash.encode('utf-8')).hexdigest()
    myresult.configure(state="normal")
    myresult.delete("1.0","end")
    myresult.insert("0.0", str(hashed))
    myresult.configure(state="disabled")    



myinput = customtkinter.CTkEntry(root, placeholder_text=("test"))
myinput.grid(row=1, column =0, padx=10, pady=10, sticky="ew")

mybutton = customtkinter.CTkButton(root, text='Calculate Hash', command=gethash)
mybutton.grid(row=2, column= 0, padx = 10, pady= 10, sticky ="ew")

#mytextbox = customtkinter.CTkTextbox(root, height=20)
#mytextbox.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
#mytextbox.configure(state="disabled")

myresult = customtkinter.CTkTextbox(root, height=10)
myresult.grid(row=3, column=0, padx = 10, pady= 10, sticky ="ew")


root.mainloop()
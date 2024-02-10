from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")



root = customtkinter.CTk()
root.title("Hash calculator")
root.geometry('400x200')

root.grid_columnconfigure(0, weight=1)

def gethash():
    tohash=myinput.get()
    hashed=hash(tohash)
    mytextbox.insert("0.0", str(hashed))
    



myinput = customtkinter.CTkEntry(root, placeholder_text=("test"))
myinput.grid(row=1, column =0, padx=10, pady=10, sticky="ew")

mybutton = customtkinter.CTkButton(root, text='Calculate Hash', command=gethash)
mybutton.grid(row=2, column= 0, padx = 10, pady= 10, sticky ="ew")

mytextbox = customtkinter.CTkTextbox(root, height=20)
mytextbox.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
mytextbox.configure(state="disabled")

root.mainloop()
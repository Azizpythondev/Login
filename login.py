import tkinter
from tkinter import *
from tkinter import PhotoImage
import webbrowser

window = tkinter.Tk()
window.title("Login")
window.geometry('340x440')
window.configure(bg="#333333")
window.resizable(False,False)

def login():
        url = 'https://github.com/Azizpythondev'
        Username = "Azizpythondev"
        password = "Aziz28011998"
        if entry.get()==Username and entry_2.get()==password:
                print("duris login")
        else:
                print("qate login")
        webbrowser.open_new_tab(url)
'''
img = tkinter.PhotoImage(file="./Documents/Python 12/forgit/13.jpg")
imgbx = tkinter.Label(image=img)
imgbx.place(x=195, y=15)
imgbx['bg'] = '#696969'''

label = tkinter.Label(window, text="Login")
label.place(x=150, y=10)

label_2 = tkinter.Label(window, text="Username / email: ", bg="#333333", fg= "white", font="Roboto 12 bold")
label_2.place(x=30, y=120)

entry = tkinter.Entry(window)
entry.place(x=60, y=150, width=200)

label_3 = tkinter.Label(window, text="Password: ", bg="#333333", fg= "white", font="Roboto 12 bold")
label_3.place(x=30, y=200)

entry_2 = tkinter.Entry(window)
entry_2.place(x=60, y=230, width=200)

Button = tkinter.Button(window, text="Login",bg="green", fg= "white", width=10, font="Roboto 12 bold", command=login)
Button.place(x=100, y=290)

label_4 = tkinter.Label(window, text="Forgut your password? ", font="Roboto 12 bold")
label_4.place(x=130, y=400)

window.mainloop()
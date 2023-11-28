import pyshorteners
from tkinter import *

win = Tk()
win.geometry("450x275")
win.configure(bg="pink")

def short():
    url = E.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    E2.insert(END, s)

Label(win, text="Enter your URL Link:", font="impact 18 normal", bg="grey", fg="black").pack(fill="x")

E = Entry(win, font="10", bd=4, width=45)
E.pack(pady=30)

# Add the command option to the button to call the 'short' function
Button(win, text="Click here", font="impact 10 normal", bg="black", fg="grey", width=8, command=short).pack()

E2 = Entry(win, font="impact 18 normal", bg="pink", width=26)
E2.pack(pady=30)

mainloop()

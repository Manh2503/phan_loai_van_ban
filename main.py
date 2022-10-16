import tkinter as tk
from tkinter import END
from tkinter import *
from turtle import Screen
import PIL
from PIL import ImageTk, Image
from numpy import size
import nbc
from tkinter import scrolledtext, Tk, BOTH, NS
window = Tk()

width = 1920
height = 1080

window.title("Hệ thống nhận dạng chủ đề văn bản")
window.state('zoomed')
window.minsize(1526,800)

frame = Frame(window, width=width, height=height)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("theme/background.png"))
label = Label(frame, image = img)
label.pack()

def clickMe():
    res.configure(text=nbc.classify(txt.get("1.0",END)))


txt = scrolledtext.ScrolledText(window,width=115,height=12)
txt.grid(column=0, row=1, padx = (312,0), pady = (340,0))

button = Button(window, text = "Kiểm tra", command = clickMe, padx = 10, pady = 10, bg='#ffde59', font=("Courier", 10))
button.grid(column=0, row = 2, padx = (300,0), pady=(30,0))


res = Label(window, text = "", bg = 'white', font=("Courier", 18))
res.grid(column = 0, row = 3, padx=(470,0), pady=(83,0))

window.mainloop()
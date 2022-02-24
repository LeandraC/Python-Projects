import sys, math
from tkinter import *

#cannot .get and button at same time

canvas = Tk()
canvas.title("Calculator")
canvas.configure(bg = 'light blue')

p=("Oswald", 12, "bold")
funs = ['+', '-', '*', '/']
spec = [0, '00', '.']

trip = ''
i = 0
c = ''
for a in range(3):
    i+=1
    Button(canvas, font = p, text=(f'{i}'), width = 5, padx=2, justify="center", command=lambda c = i: click(c)).grid(column=(a+1), row =(3), sticky="news")
    Button(canvas, font = p, text=(f'{i+3}'), width = 5, padx=2, justify="center", command=lambda c = i: click(c)).grid(column=(a+1), row =(2), sticky="news")
    Button(canvas, font = p, text=(f'{i+6}'), width = 5, padx=2, justify="center", command=lambda c = i: click(c)).grid(column=(a+1), row =(1), sticky="news")


for i,k in enumerate(spec):
    Button(canvas, font = p, text = (f'{k}'), width = 5, padx=2, command=lambda c=k: click(c)).grid(column =(i+1), row = 4)

for i, k in enumerate(funs):
    Button(canvas, font=p, text = (f'{k}'), width = 5, padx=2, command = lambda c=k: click(c)).grid(column=4, row = (i+1))

Button(canvas, font = p, text = 'Clear', width = 5, padx=2, command = lambda:clear()).grid(column=4, row =5)
Button(canvas, font = p, text = '=', width = 5, padx=2, command = lambda: give()).grid(column=3, row =5)
Button(canvas, font = p, text = 'Exit', width = 5, padx=2, command = lambda: quit()).grid(column=1, row =5)

boop=Entry(canvas, font=p, width=5, justify= "right", bg="red")
boop.grid(columnspan = 5, ipadx=90, row = 0)
boop.focus()
boop.icursor(END)
bloop = boop.get()
logged = StringVar()
bebop = boop.config(textvariable = logged)


def strokes(event):
    global c
    c = boop.get()
    boop.delete(0,END)
    boop.icursor(END)
    click(c)
    c=' '
    give()


def click(c):
    global trip, logged
    boop.icursor(END)
    boop.delete(0,END)
    trip += str(c)
    logged.set(trip)
    bebop


def give():
    global trip
    equal = str(eval(trip))
    trip = ''
    logged.set(equal)
    boop.icursor(END)
    bebop


def clear():
    global trip, c
    boop.icursor(END)
    trip=''
    c=''
    logged.set(trip)
    boop.delete(END)
    bebop




canvas.bind('<Return>', strokes)
boop.icursor(END)
canvas.mainloop()


import sys, math
from tkinter import *

#cannot .get and button at same time
#wip, will be updated

canvas = Tk()
canvas.title("Calculator")
canvas.configure(bg = 'light blue')

p=("Oswald", 12, "bold")
funs = ['+', '-', '*', '/']
spec = [0, '00', '.']

trip = ''
i = 0
for a in range(3):
    for b in range(3):
        i+=1
        Button(canvas, font = p, text=(f'{i}'), width = 5, padx=2, justify="center", command=lambda c=i: click(c)).grid(column=(b+1), row =(a+1), sticky="news")

for i,k in enumerate(spec):
    Button(canvas, font = p, text = (f'{k}'), width = 5, padx=2, command=lambda c=k: click(c)).grid(column =(i+1), row = 4)

for i, k in enumerate(funs):
    Button(canvas, font=p, text = (f'{k}'), width = 5, padx=2, command = lambda c=k: click(c)).grid(column=4, row = (i+1))

Button(canvas, font = p, text = 'Clear', width = 5, padx=2, command = lambda:clear()).grid(column=4, row =5)
Button(canvas, font = p, text = '=', width = 5, padx=2, command = lambda: give()).grid(column=3, row =5)
Button(canvas, font = p, text = 'Exit', width = 5, padx=2, command = lambda: quit()).grid(column=1, row =5)

boop=Label(canvas, font=p, width=5, anchor= 'e', bg="red")
boop.grid(columnspan = 5, ipadx=90,row = 0)
logged = StringVar()
bebop = boop.config(textvariable = logged)




def click(c):
    global trip, logged
    trip += str(c)
    logged.set(trip)
    bebop


def give():
    equal = str(eval(trip))
    logged.set(equal)
    bebop

def clear():
    global trip
    trip=''
    logged.set(trip)
    bebop



canvas.mainloop()

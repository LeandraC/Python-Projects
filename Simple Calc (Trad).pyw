import sys, math
from tkinter import *

canvas = Tk()
canvas.title("Calculator")
canvas.configure(bg = 'light blue')
canvas.geometry('260x180')
canvas.resizable(False, False)
entry_lvl = Frame(canvas, width = 200, height = 30, bg = "light blue")
entry_lvl.place(relx = .5, rely = .1, anchor = "center")
key_lvl = Frame(canvas, width = 200)
key_lvl.place(relx = .02, rely = .2)
function_lvl = Frame(canvas)
function_lvl.place(relx = .74, rely = .2)

p=("Oswald", 12, "bold")
funs = ['+', '-', '*', '/']
spec = [0, '00', '.']

trip = ''
i = 0
c = ''
for a in range(3):
    i+=1
    Button(key_lvl, font = p, text=(f'{i}'), width = 5, padx=2, justify="center", command=lambda c = i: click(c)).grid(column=(a+1), row =(3), sticky="news")
    Button(key_lvl, font = p, text=(f'{i+3}'), width = 5, padx=2, justify="center", command=lambda c = (i + 3): click(c)).grid(column=(a+1), row =(2), sticky="news")
    Button(key_lvl, font = p, text=(f'{i+6}'), width = 5, padx=2, justify="center", command=lambda c = (i + 6): click(c)).grid(column=(a+1), row =(1), sticky="news")


for i,k in enumerate(spec):
    Button(function_lvl, font = p, text = (f'{k}'), width = 5, command = lambda: click(k)).grid(column =(4), row = (i + 1))

for i, k in enumerate(funs):
    Button(function_lvl, font=p, text = (f'{k}'), width = 5, padx=2, command = lambda c=k: click(c)).grid(column=4, row = (i+1))

Button(key_lvl, font = p, text = 'Clear', width = 5, padx=2, command = lambda:clear()).grid(column=2, row =5)
Button(key_lvl, font = p, text = '=', width = 5, padx=2, command = lambda: give()).grid(column=3, row =5)
Button(key_lvl, font = p, text = 'Exit', width = 5, padx=2, command = lambda: quit()).grid(column=1, row =5)

manual_entry = StringVar()
entre= Entry(entry_lvl, textvariable = manual_entry, font=p, justify= "right", bg="red", fg = "white")
entre.place(relx = .5, rely = .5, anchor = "center", relwidth = 1, relheight = 1)
manual_entry.set('0')


def strokes(event):
    c = entre.get() + str(event)
    entre.delete(0,END)
    entre.icursor(END)
    click(c)
    c=' '
    give()


def click(c):
    global trip, manual_entry
    entre.icursor(END)
    entre.delete(0,END)
    trip += str(c)
    manual_entry.set(trip)



def give():
    global trip
    equal = str(eval(trip))
    trip = ''
    manual_entry.set(equal)
    entre.icursor(END)



def clear():
    global trip, c
    entre.icursor(END)
    trip=''
    c=''
    manual_entry.set(trip)
    entre.delete(END)




canvas.bind('<Return>', strokes)
entre.icursor(END)
canvas.mainloop()


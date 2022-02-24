import sys, random
from tkinter import *

rand = random.randint(1,10)
points = 0
score = 0
wins = 0
guess = ' '
a = rand
b = 0




canvas = Tk()
canvas.title('Higher or Lower')

label1 = Label(canvas)
label1.grid(column = 2, row = 5)
label2 = Label(canvas)
label2.grid(column = 2, row = 6)

Button(text="Higher", width = 10, command = lambda: nums('higher')).grid(column = 1, row = 6)
Button(text="Lower", width = 10, command = lambda: nums('lower')).grid(column = 3, row = 6)
Button(text = 'Quit', width = 10, command = lambda: sys.exit()).grid(column = 2, row = 9)

def current():
    global b
    label1.config(text = (f'Current number: {a}'))
    b = random.randint(1,10)
    if b == a:
        current()

def winMax():
    global wins
    if wins >= points:
        Label(text = (f"Max score: {wins} points!")).grid(column = 1, row = 7)
    else:
        wins = points
        Label(text = (f"Max score: {points} points!")).grid(column = 1, row = 7)



def nums(guess):
    global a, b, points, score
    label1.config(text = (f'Current number: {a}'))
    if guess == 'higher':
        if b >= a:
            label2.config(text = (f"You guessed correctly! {b} was higher than {a}!"))
            score += 1
            if score >= 3:
                points += 1
        if b <= a:
            label2.config(text = (f"Too bad. {b} was not higher than {a}."))
            winMax()
            points = 0
            score = 0
    if guess == 'lower':
        if b <= a:
            label2.config(text = (f"You guessed correctly! {b} was lower than {a}!"))
            score += 1
            if score >= 3:
                points += 1
        if b >= a:
            label2.config(text = (f"Too bad. {b} was not lower than {a}."))
            winMax()
            points = 0
            score = 0
    a = b
    current()
    Label(text = (f'You\'ve had {score} right in a row!')).grid(column = 2, row = 3)
    Label(text = (f"You now have {points} points!")).grid(column = 3, row = 7)




def Game():
    current()
    Label(text = ('Hello there, friend! Let\'s play a number game!')).grid(column = 2, row = 1)
    Label(text = ('I\'m going to say a number between 1 and 10, then I\'ll pick another number between 1 and 10.')).grid(column = 2, row = 2)
    Label(text = (f'First number is {a}!')).grid(column = 2, row = 3)
    Label(text = ('Will the next number be (h)igher or (l)ower?')).grid(column = 2, row = 4)
    if guess.lower() == 'h' or guess.lower() == 'higher':
        nums('higher')
    if guess.lower() == 'l' or guess.lower() == 'lower':
        nums('lower')
    if score >= 5:
        Label(text = "You win! You have 5 points! You can keep playing if you like.").grid(column = 5, row = 3, columnspan = 2)

Game()

canvas.mainloop()

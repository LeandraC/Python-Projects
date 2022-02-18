import random, sys
from tkinter import *

canvas = Tk()
canvas.title("Coin Toss")
canvas.geometry("225x125")
coin = ["heads", "tails", "lost"]
toss = random.randint(0,2)
flip = coin[toss]
cg = random.choice(coin)
pScore = 0
cScore = 0

pS = Label(canvas, text = pScore, width = 5)
pS.grid(column = 0, row = 6)
cS = Label(canvas, text = cScore, width = 5)
cS.grid(column = 2, row = 6)

chat= Label(canvas)
chat.grid(column=0, columnspan = 3, row = 0, rowspan = 2)
chat2= Label(canvas)
chat2.grid(column=0, columnspan = 3, row = 2, rowspan = 2)

for i, k in enumerate(coin):
    Button(text = k, width = 5, command = lambda c = k: choice(c)).grid(column = i, row = 5)

Button(canvas, text = 'Quit', width = 5, command = lambda: Quit()).grid(column=1, row = 6)

def Quit():
    sys.exit()

def choice(c):
    global pScore, cScore
    flip= coin[(random.randint(0,2))]
    cg = random.choice(coin)
    if c == flip:
        chat.config(text = f"The coin landed on {flip}.\nYou guessed {c}! That\'s 1 point for you!")
        pScore +=1
    if c != flip:
        chat.config(text = f"The coin landed on {flip}.\nYou guessed {c}! Better luck next time.")
    if cg == flip:
        chat2.config(text = f'I guessed {cg}.\nThat\'s 1 point for me!')
        cScore += 1
    if cg != flip:
        chat2.config(text = f'I guessed {cg}.\nAw, biscuits! I\'ll get it next time!')
    if c == "lost":
        if flip == "lost":
            chat.config(text= 'Oh, no! I lost the coin!')
            chat2.config(text = "Why'd you throw it away?!")
        elif flip != "lost":
            chat.config(text = f'Ha! You missed!\nThe coin landed on {flip}!')
            chat2.config(text = 'I get 1 point because\nyou tried to cheat!')
            cScore += 1
        else:
            chat2.config(text = 'Let\'s try this again.')
    pS.config(text = pScore)
    cS.config(text = cScore)

chat.config(text = "\nLet\'s play coin toss! I\'ll flip a coin!")
chat2.config(text = "Pick heads or tails!")



canvas.mainloop()

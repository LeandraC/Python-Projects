import random, sys, time
coin = ['heads', 'tails']
bye = ['q', 'quit', 'e', 'exit']
ps = 0
cs = 0
breathe = time.sleep(.5)

def Quit():
    quit()

def Play(c):
    global ps, cs
    flip = random.choice(coin)
    cg = random.choice(coin)
    if c == flip:
        print(f'You guessed {c} and the coin landed on {flip}!')
        breathe
        print('That\'s 1 point for you!')
        ps += 1
    elif c != flip:
        print(f'You guessed {c} and the coin landed on {flip}!')
        breathe
        print('Better luck next time.')
    if cg == flip:
        print(f'I guessed {cg} and the coin landed on {flip}!')
        breathe
        print('That\'s 1 point for me!')
        cs += 1
    elif cg != flip:
        print(f'I guessed {cg} and the coin landed on {flip}!')
        breathe
        print('I\'ll get it next time!')
    if c.lower() in bye:
        Quit()
    print(f'Player: {ps} vs Computer: {cs}.')

while True:
    print("Would you like to play a game?")
    time.sleep(1)
    print("Let\'s play coin toss!\nType (Q)uit to exit at any time.")
    time.sleep(1)
    c = input("Pick (h)eads or (t)ails.")
    if c.lower() == 'heads' or c.lower() == 'h':
        c = 'heads'
        Play(c)
    elif c.lower() == 't' or c.lower() == 'tails':
        c = 'tails'
        Play(c)
    elif c.lower() in bye:
        quit()

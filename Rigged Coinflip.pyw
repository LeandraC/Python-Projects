import random, sys, time

coin = ['heads', 'tails']
flip = random.randint(1,2)-1
pscore = 0
cscore = 0
cg = random.randint(1,2)-1
coinflip = coin[flip]

def pguess(x):
    global pscore
    global cscore
    print(f'The coin lands on {coinflip}')
    time.sleep(.2)
    if coin[x] == coinflip:
        print('Good guess! That\'s 1 point for you!')
        pscore += 1
    if coin[x] != coinflip:
        print('Better luck next time.')
    time.sleep(.2)
    if coin[cg] == coinflip:
        print('That\'s one point for me!')
        cscore += 1
    if coin[cg] != coinflip:
        print('Aw, biscuits! I\'ll get it next time!')
    print(f'That\'s {pscore} points for you vs {cscore} points for me!')


while True:
    pg = input('I\'ll flip a coin. Guess (h)eads or (t)ails.')
    if pg.lower() == 'heads' or pg.lower() == 'h':
        x = 0
        print(f'You guess {coin[x]}.')
        time.sleep(.2)
        print(f'I\'ll guess {coin[cg]}!')
        time.sleep(.2)
        pguess(x)

    elif pg.lower() == 'tails' or pg.lower() =='t':
        x = 1
        print(f'You guess {coin[x]}.')
        time.sleep(.2)
        print(f'I\'ll guess {coin[cg]}!')
        time.sleep(.2)
        pguess(x)
    
    else:
        time.sleep(1)
        print('You must be tired. Come back when you want to play again!')
        time.sleep(1)
        sys.exit()

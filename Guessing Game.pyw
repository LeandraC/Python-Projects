import random, sys

lives = 0
y = 0
hello = ' '


def guess(x):
	y = 0
	global lives
	high = x
	rand = random.randint(1,x)
	while y != rand and lives > 0:
		try:
			y = int(input(f'Choose a number between 1 and {x}.'))
		except ValueError:
			input('Please enter a valid number or type Q to quit.')
			if input().lower() == 'q':
				sys.exit()
			else:
				y = int(input())
		if y < rand:
			print(f'Ah ah ah, {y} is too low')
			lives -= 1
		if y > rand:
			print(f'Ah ah ah, {y} is too high')
	if lives == 0:
			print(f'Too bad. There are no more guesses! The correct number was {rand}.')
	print(f'Hooray! You guessed {rand}, which WAS the number! AND you got it right with {lives} guesses left!')

def comp(x):
	global lives
	low = 1
	high = x
	squanch = ' '
	c = 0
	while squanch != 'c' and lives > 0:
		c = (random.randint(low, high))
		try:
			squanch = input(f'I guess {c}. is {c} too (h)igh or too (l)ow or (c)orrect?').lower()
		except ValueError:
			y = input('Please enter a valid response or type Q to quit.').lower()
			if y == 'q':
				sys.exit()
		if squanch == 'l':
			low = c + 1
			lives -= 1
		if squanch == 'h':
			high = c - 1
			lives -= 1
		if low == high:
			c = low
	if lives == 0:
		print('Ah, nuts! I used up all my guesses. I\'ll get it next time!')
	print(f'Hooray! I guessed {c}, which WAS the number! AND I got it right with {lives} guesses left!')

while True:
	hello = (input('Hello there! Let\'s play a guessing game!\
	\nEnter U for you guess my number, C for I guess your number or press Q to quit.')).lower()
	if hello == 'q':
		sys.exit()
	x = int(input('Please pick a max number.'))
	lives = (x*2)//10
	if hello == 'c':
		comp(x)
	if hello == 'u':
		guess(x)
	else:
		print('Please enter a valid response.')

import sys, time, random

won = 0
lost = 0
tie = 0
computer = 0
def delay(s):
	for c in s:
		sys.stdout.write(c)
		time.sleep(.1)
moves = ['rock', 'paper', 'scissors']

while True:
	print(f'{won} wins, {lost} losses, {tie} ties.')
	for i, k in enumerate(moves):
		print(f'{i+1}.', k)
	try:
		player = int(input(delay('Pick your move!')))
	except ValueError or IndexError:
		v = input(print('Please enter a valid response. Unless you meant quit.\
		\nWould you like to quit? Press Y to quit or enter a valid number to continue.'))
		if v.lower() == 'q' or 'y':
			sys.exit()
		else:
			v = int(v)
			shoot(v)
	computer = random.randint(1,3)
	print(f'{moves[(player-1)]} vs {moves[(computer-1)]}!')
	if (player+1)%3 is computer-1:
		won += 1
		print('You won!')
	if (player+3)%3 is computer-1:
		lost += 1
		print('I won!')
	if player is computer:
		tie += 1
		print('That\'s a tie.')

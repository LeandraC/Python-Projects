import sys, time, random, string
from words import words

def hangman():
	word = (random.choice(words)).upper()
	word_letters = set(word)
	alphabet = set(string.ascii_uppercase)
	lives = len(word)
	used_letters = set()
	print('*At any time type quit to exit*.')
	while len(word_letters) and lives > 0:
		print(f'You have {lives} left and have used these letters: ' , ' '.join(used_letters))
		word_list = [letter if letter in used_letters else '-' for letter in word]
		print('Current word: ', ' '.join(word_list))
		guess = input('Guess a letter or word: ').upper()
		if guess == word:
			break
		if guess in alphabet - used_letters:
			used_letters.add(guess)
			if guess in word_letters:
				word_letters.remove(guess)
				print(' ')
			elif guess != word:
				print(f'{guess} is not the word. Please try again.')
				used_letters.add(guess)
				lives -= 1
		elif guess in used_letters:
			print(f'You have already used {guess}.')
		elif guess == 'QUIT':
			goodbye = input('Would you like to quit?\
			\n Press q to quit.').lower()
			if goodbye is 'y' or 'q':
				sys.exit()
		else:
			print('Invalid character. Please try again.')
		if lives is 1:
			print('Last guess!')
	if lives is 0:
		print('What a lovely necklace...')
		print(f'The word was {word}.')
	else:
		print(f'Good game! You guessed the word {word} with {lives} lives left out of {len(word)}!!')

while True:
	hello = input(print('Hello! Would you like to play a word guessing game?\
    \nYou can guess a random pokemon name!\
    \nPress Y to continue or Q to quit.')).lower()
	if hello == 'y':
		hangman()
	elif hello != 'y':
		hello == input('Did you wish to quit? Type Q to quit or enter a valid response to continue.').lower()
		if hello == 'q':
			sys.exit()

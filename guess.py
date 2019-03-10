import random
lower_bnd = input('Enter an integer as a lower bound: ')
upper_bnd = input('Enter an integer as a upper bound: ')
lower_bnd = int(lower_bnd)
upper_bnd = int(upper_bnd)


r = random.randint(lower_bnd, upper_bnd)
try_number = 0

while True:
	print('Enter an integer btw ',lower_bnd,' and ', upper_bnd, ': ')
	guess = input()
	guess = int(guess)
	if guess > r:
		print('the number is smaller than what you guessed, pls try again.')
		try_number = try_number + 1
	elif guess < r:
		print('the number is larger than what you guessed, pls try again.')
		try_number = try_number + 1
	else:
		print('congradulation! The number is ', r)
		try_number = try_number + 1
		print('you tried ', try_number, 'times')
		break

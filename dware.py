'''
Diceware password generator - created for educational purposes only!
'''
from random import SystemRandom #More cryptographically secure random number generation
from dicewarewords import words 

def get_key():
	'''
	Returns a 5 digit number as a string.
	Said string is composed of numbers from 1-6 inclusive, thereby simulating 5 die rolls
	'''
	return ''.join([str(SystemRandom().randrange(6)+1) for i in range(5)])

def get_password(num_of_words = 5):
	return ''.join([words[get_key()] for i in range(num_of_words)])

def get_options():
	num, special_char = '', ''

	while num != 'y' and num != 'n':
		num = input('Do you numbers included to strengthen your password? [y/n] ').lower()

	while special_char != 'y' and special_char != 'n':
		special_char = input('Do you wish to add random special characters (like @, #, + etc) to strengthen your password? [y/n] ').lower()

	return num, special_char

def edit_pwd(edit, pwd):
	#Choose how many special characters to add (1-3)
	num_of_nums = SystemRandom().randrange(3)+1
	#Add random nums in random positions
	for i in range(num_of_nums):
		pos = SystemRandom().randrange(len(pwd))
		pwd = pwd[:pos] + edit + pwd[pos:]
	return pwd


if __name__ == '__main__':
	pwd = get_password()
	
	n, s_c = get_options()
	#Print the vanilla/base password first since that's easier to remember
	if n == 'y' or s_c == 'y':
		print('The base password is: ' + pwd)

	#Add random numbers
	if n == 'y':
		pwd = edit_pwd(str(SystemRandom().randrange(10)), pwd)

	#Add random characters
	if s_c == 'y':
		pwd = edit_pwd(chr(SystemRandom().randrange(11) + 35), pwd)

	print(pwd)
	

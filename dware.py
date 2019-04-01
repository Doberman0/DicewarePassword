'''
Diceware password generator - created for educational purposes only!
'''
import random as r #replace with more random OS module
from dicewarewords import words 

def get_key():
	'''
	Returns a 5 digit number as a string.
	Said string is composed of numbers from 1-6 inclusive, thereby simulating 5 die rolls
	'''
	return ''.join([str(r.randint(1,6)) for i in range(5)])

def get_password():
	#key = get_key()
	#print(words[get_key()])
	return ''.join([words[get_key()] for i in range(5)])

if __name__ == '__main__':
	#get_word()
	print(get_password())
	
#Script to make a dictionary of words and their key
f = open('dicewarewords.txt', 'r')
words = {}
for line in f:
	l = line[:-1].split('\t')
	words[l[0]] = l[1]
f.close()

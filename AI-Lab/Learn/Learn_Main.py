from __future__ import print_function

import random_in_wordlist.py as choose

def learn(x,x_to):
	blank = ' '
	to_write_on_file = x + blank + x_to
	to_write_on_file_inverse = x_to + blank + x
	if x in open('brain.txt').read():
		choose.choose('Error','no','maybe')
	else:
		brain = open('brain.txt', 'a')
		print(to_write_on_file, file=brain)
		print(to_write_on_file_inverse, file=brain)
		brain.close()

def research(x,x_to):
	blank = ' '
	to_write_on_file = x + blank + x_to
	to_write_on_file_inverse = x_to + blank + x
	if x in open('brain.txt').read():
		print('true')
	else:
		pass

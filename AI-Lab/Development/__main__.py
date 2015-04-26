#!/usr/bin/python
#[P]seudo
#[I]ntelligent
#[N]neural
#[N]network
import Speak

from time import sleep
import os

os.system('clear')
Speak.speak("Hello again")
Speak.speak('Here you found all the development tool you will need')
print('Good Luck')
print('\n')
print('This is a list of all commands:')
print('Python - The python command line')
print('Bash - The Linux command line')
print('Exit - Exit this application')

user_input = raw_input('Command >>> ')
user_input = user_input.upper()

if user_input == 'PYTHON':
	Speak.speak("Starting Python")
	Speak.speak("If you need some help, please type help in the terminal, here is a clue")
	os.system('clear')
	print("help()")
	os.system('python')
elif user_input == 'BASH':
	Speak.speak("Starting Bash")
	Speak.speak("If you need some help, please type Help in the terminal")
	os.system('clear')
	os.system('bash')
elif user_input == 'EXIT':
	os.system('clear')
	print('Bye')
	Speak.speak("Bye")
else :
	print('Sorry I did not understand')
	Speak.speak("Sorry I did not understand")

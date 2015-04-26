#!/usr/bin/python
#[P]seudo
#[I]ntelligent
#[N]neural
#[N]network

import os
import numpy
import time
import thread
import threading
import sys
import serial
import speak
import minimax_tic_tac_toe

serial = serial.Serial('/dev/ttyACM0', 9600)
serial.write('3')

os.system("clear")

random = numpy.random.randint(1, 3)

def raw_input_with_timeout(prompt, timeout=14):    
    timer = threading.Timer(timeout, thread.interrupt_main)
    astring = None
    try:
        timer.start()
        astring = raw_input(prompt)
    except KeyboardInterrupt:
        pass
    timer.cancel()
    for char in astring:
     time.sleep(0.2)
     sys.stdout.write(char)
     sys.stdout.flush()

    return astring


if True:
  	serial.write('4')
	print("[P]robably")
	print("[I]ntelligent")
	print("[N]neural")
	print("[N]network")
	speak.speak("The main core have been started successfully")
	speak.speak("Administrator please, input your command")
	user_input = raw_input_with_timeout("Command ")
	user_input = user_input.upper()
	serial.write('5')
	time.sleep(1)
	if user_input == 'DEBUG':
	    serial.write('4')
	    time.sleep(1)
	    serial.write('5')
	    time.sleep(0.2)
	    speak.speak("Developer Mode Started")
	    os.system('python Development/')#call the development module
	elif (user_input == 'TIC TAC TOE' or user_input == 'TICTACTOE' or user_input == 'GAME' or user_input == 'PLAY'):
		os.system('clear')
		serial.write('4')
		speak.speak("Let's play Tic Tac Toe")
		speak.speak("Remember, you are the X, I am the O")
		speak.speak("Good Luck")
		if random == 2:
			speak.speak("or not")
		os.system('python minimax_tic_tac_toe.py')
		serial.write('5')
	elif user_input == 'EXIT':
	    speak.speak("Good Bye")
	elif (user_input == 'RESTART' or user_input == 'RESET'):
	    speak("Restarting now")
	elif (user_input == 'HELP'):
	    speak.speak("module in development, sorry.")
	    os.system('python Help/')#call the help module
	elif (user_input == 'SHUTDOWN'):
	    speak.speak("Shutting down now")
	    speak.speak("Bye Bye")
	    os.system("sudo shutdown -h now")

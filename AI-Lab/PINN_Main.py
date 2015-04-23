#Copyright (C) 2015 Gabriel de Oliveira <gabriel.oli01001@gmail.com>
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

serial = serial.Serial('/dev/ttyACM0', 9600)
serial.write('3')

os.system("clear")

random = numpy.random.randint(1, 3)

def speak(n):
    speech = 'espeak -ven-uk-rp -v female3 -k5 -s150' + ' ' + '"' + n + '"' + " 2>/dev/null"
    print speech
    os.system(speech)

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
	print("[P]seudo")
	print("[I]ntelligent")
	print("[N]neural")
	print("[N]network")
	speak("The main core have been started successfully")
	speak("Beware world, I am Alive")
	speak("Administrator please, input your command")
	user_input = raw_input_with_timeout("Command ")
	user_input = user_input.upper()
	serial.write('5')
	time.sleep(1)

	if user_input == 'DEBUG':
	    serial.write('4')
	    time.sleep(1)
	    serial.write('5')
	    time.sleep(0.2)
	    speak("Developer Mode started")
	elif user_input == 'EXIT':
	    speak("ok")
	elif (user_input == 'RESTART' or user_input == 'RESET'):
	    speak("done")

import os
def speak(n):
    n = '"' + n
    n = n + '"'
    speech = 'pico2wave -w outvoice.wav -l en-GB ' + n + " && aplay outvoice.wav && rm outvoice.wav"
    print speech
    os.system(speech)

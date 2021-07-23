from bluedot import BlueDot
from signal import pause

bd = BlueDot()

def say_hello():
    print("Hello World")

bd.when_pressed = say_hello

pause()
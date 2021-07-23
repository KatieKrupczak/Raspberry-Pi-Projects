from bluedot import BlueDot
from signal import pause

bd = BlueDot()

def say_hello():
    print("Hello")

bd.when_double_pressed = say_hello

pause()
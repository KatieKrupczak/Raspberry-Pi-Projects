from bluedot import BlueDot
from signal import pause

bd = BlueDot()

def say_hello():
    print("Hello World")

def say_goodbye():
    print("Goodbye")

bd.when_pressed = say_hello
bd.when_released = say_goodbye

pause()
from gpiozero import Button
from signal import pause

button = Button(2)

def say_hello():
    print("Hello!")
    
def say_goodbye():
    print("Goodbye!")

button.when_pressed = say_hello
button.when_released = say_goodbye

pause()
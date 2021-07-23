from bluedot import BlueDot
from signal import pause

def pressed_1():
    print("button 1 pressed")

def pressed_2():
    print("button 2 pressed")

bd = BlueDot(cols=3, rows=1)
bd[1,0].visible = False

bd[0,0].when_pressed = pressed_1
bd[2,0].when_pressed = pressed_2

pause()
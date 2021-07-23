from bluedot import BlueDot
from gpiozero import LEDBoard
from signal import pause

bd = BlueDot(cols=1, rows=10)
leds = LEDBoard(2,3,4,17,27)

#spacer buttons
for i in range(1, 10, 2):
    bd[0,i].visible = False

#set color for visible buttons
bd[0,0].color = "red"
bd[0,2].color = "yellow"
bd[0,4].color = "green"
bd[0,6].color = "blue"
bd[0,8].color = "gray"

#set leds to button values
for i in range(5):
    leds[i].source = bd[0,2*i].values

pause()
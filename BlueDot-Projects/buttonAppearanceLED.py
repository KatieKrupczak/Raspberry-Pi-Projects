from bluedot import BlueDot
from gpiozero import LED
from signal import pause

bd = BlueDot()
led = LED(2)

#changing button appearance
bd.color = "red"
bd.square = True

led.source = bd.values

pause()
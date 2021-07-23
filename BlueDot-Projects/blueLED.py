from bluedot import BlueDot
from gpiozero import LED
from signal import pause

bd = BlueDot()
led = LED(2)

led.source = bd.values

pause()
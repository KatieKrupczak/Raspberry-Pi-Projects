from gpiozero import LED
from signal import pause

red = LED(2)

red.blink(0.5,0.5)
pause()
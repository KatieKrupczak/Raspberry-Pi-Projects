from gpiozero import LED
from signal import pause

red = LED(17)

red.blink(0.5,0.5)
pause()
from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(3)

while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)
    buzzer.beep()
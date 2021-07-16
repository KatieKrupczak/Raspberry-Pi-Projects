from gpiozero import RGBLED
from time import sleep

led = RGBLED(red = 2, green=4, blue=3)

led.red = 1 #full red
sleep(2)
led.red = 0.5 #half red
sleep(2)

led.color = (0,1,0) #full green
sleep(2)
led.color = (1, 0, 1) #magenta
sleep(2)
led.color = (1, 1, 0) #yello
sleep(2)
led.color = (0, 1, 1) #cyan
sleep(2)
led.color = (1, 1, 1) #white
sleep(2)

led.color = (0, 0, 0) #off
sleep(2)

#slowly increase intensity of blue
for n in range(100):
    led.blue = n/100
    sleep(0.1)
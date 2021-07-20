from gpiozero import PingServer, LEDBoard
from gpiozero.tools import negated
from signal import pause

status = LEDBoard (
    columbia = LEDBoard(red=15, green=14),
    uncasville = LEDBoard(red=27, green=17),
    mankato = LEDBoard(red=24, green=23),
    nas = LEDBoard(red=9, green=10)
)

statuses = {
    PingServer('10.0.2.78'): status.columbia,
    PingServer('10.0.2.79'): status.uncasville,
    PingServer('76.217.118.132'): status.mankato,
    PingServer('10.0.2.80'): status.nas
}

for server, leds in statuses.items():
    leds.green.source = server
    leds.green.source_delay = 60
    leds.red.source = negated(leds.green)

pause()
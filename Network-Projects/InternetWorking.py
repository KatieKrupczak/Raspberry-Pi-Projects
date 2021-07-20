from gpiozero import LED, PingServer
from gpiozero.tools import negated
from signal import pause

green = LED(2)
red = LED(3)

google = PingServer('google.com')

green.source = google.values
red.source = negated(green)

pause()
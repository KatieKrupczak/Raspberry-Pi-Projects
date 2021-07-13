from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

buttonPreview = Button(2)
buttonCapture = Button(3)
camera = PiCamera()

def capture():
    #timestamp provides the title for the picture taken
    timestamp = datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % timestamp)
    
buttonPreview.when_pressed = camera.start_preview
buttonPreview.when_released = camera.stop_preview

buttonCapture.when_pressed = capture

pause()
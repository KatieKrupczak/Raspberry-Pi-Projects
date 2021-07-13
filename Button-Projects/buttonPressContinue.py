from gpiozero import Button

button = Button(2)
pressed = 0

while True:
    button.wait_for_press()
    print("Button was pressed")
    pressed += 1
    print("Press count:",pressed)
    button.wait_for_release()

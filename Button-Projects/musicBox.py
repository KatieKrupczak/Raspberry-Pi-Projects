from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()

button_sounds = {
    Button(2): Sound("gpio-music-box/samples/drum_tom_mid_hard.wav"),
    Button(3): Sound("gpio-music-box/samples/drum_cymbal_open.wav"),
    Button(4): Sound("gpio-music-box/samples/sn_generic.wav"),
    Button(17): Sound("gpio-music-box/samples/drum_cowbell.wav")    
}

for button, sound in button_sounds.items():
    button.when_pressed = sound.play

pause()
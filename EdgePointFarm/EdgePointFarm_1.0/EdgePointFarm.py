#Edge Point Farm ist ein Programm welches dazu dient Punkte im Edge Browser zu erhalten.
#Diese Punkte kann für Echtgeld Gutscheine oder anderweitige Belohnungen eintauschen.
#nur für Windows 11 auf einen Bildschirm mit der Auflösung 1920 1080
#Version: 1.0
#Autor: Dario Sellke

import time
import keyboard
from pynput.mouse import Button, Controller
import random, string

mouse = Controller()

def rnd_word(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def EPF_start(__sleep__):
    mouse.position = (700, 160)
    mouse.click(Button.left, 1)
    keyboard.write(rnd_word(5))
    time.sleep(__sleep__)
    mouse.position = (1300, 150)
    mouse.click(Button.left, 1)
    time.sleep(__sleep__)
    mouse.position = (305, 17)
    mouse.click(Button.left, 1)
    time.sleep(__sleep__)
    mouse.position = (700, 160)
    mouse.click(Button.left, 1)
    keyboard.write(rnd_word(5))
    time.sleep(__sleep__)
    mouse.position = (1300, 150)
    mouse.click(Button.left, 1)
    mouse.position = (305, 17)
    mouse.move(230, 0)
    time.sleep(__sleep__)
    mouse.position = (543, 22)
    time.sleep(0.1)
    mouse.click(Button.left, 1)
    time.sleep(__sleep__)
    mouse.position = (700, 160)
    mouse.click(Button.left, 1)
    keyboard.write(rnd_word(5))
    time.sleep(__sleep__)
    mouse.position = (1300, 150)
    mouse.click(Button.left, 1)
    time.sleep(__sleep__)
    mouse.position = (783, 12)
    mouse.click(Button.left, 1)
    time.sleep(__sleep__)
    mouse.position = (700, 160)
    mouse.click(Button.left, 1)
    keyboard.write(rnd_word(5))
    time.sleep(__sleep__)
    mouse.position = (1300, 150)
    mouse.click(Button.left, 1)
    time.sleep(__sleep__)
    mouse.position = (1896, 16)
    mouse.click(Button.left, 1)

print("Press Ctrl to start!")
keyboard.wait("ctrl")
EPF_start(1.5)
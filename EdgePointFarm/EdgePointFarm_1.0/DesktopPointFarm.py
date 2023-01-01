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

def EPFD_start(__sleep__):
    for i in range(31):
        mouse.position = (800, 1060)
        time.sleep(__sleep__)
        mouse.click(Button.left, 1)
        time.sleep(__sleep__)
        keyboard.write(rnd_word(5))
        time.sleep(__sleep__)
        keyboard.press("enter")
        time.sleep(__sleep__)
        mouse.position = (1896, 16)
        mouse.click(Button.left, 1)
        time.sleep(__sleep__)

EPFD_start(1)
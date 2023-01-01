import time
import keyboard
from pynput.mouse import Button, Controller
import random, string

mouse = Controller()

def rnd_word(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

#Desktop
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
#5x sleep 31 mal

#Browserf
def EPF_start(__sleep__):
    mouse.position = (700, 160)
    mouse.click(Button.left, 1)
    keyboard.write(rnd_word(7))
    time.sleep(__sleep__)
    mouse.position = (1300, 150)
    mouse.click(Button.left, 1)
    time.sleep(__sleep__)
    mouse.position = (305, 17)
    mouse.click(Button.left, 1)
    time.sleep(__sleep__)
    mouse.position = (700, 160)
    mouse.click(Button.left, 1)
    keyboard.write(rnd_word(7))
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
    keyboard.write(rnd_word(7))
    time.sleep(__sleep__)
    mouse.position = (1300, 150)
    mouse.click(Button.left, 1)
    time.sleep(__sleep__)
    mouse.position = (783, 12)
    mouse.click(Button.left, 1)
    time.sleep(__sleep__)
    mouse.position = (700, 160)
    mouse.click(Button.left, 1)
    keyboard.write(rnd_word(7))
    time.sleep(__sleep__)
    mouse.position = (1300, 150)
    mouse.click(Button.left, 1)
    time.sleep(__sleep__)
    mouse.position = (1896, 16)
    mouse.click(Button.left, 1)

#12x sleep 1 mal

_E1 = "The sleep value can't be und 3 seconds!"

def Error(_error):
    
    if _error == _E1:
        print(_error)
        


__sleep__=float(input("Input the time to wait between tasks: "))

if __sleep__ < 3:

    Error(_E1)
    print("an Error occured")
    time.sleep(0.5)
    print("check the .log file")
    time.sleep(0.5)
    print("Program is closing")
    time.sleep(1)
    exit()

else:

    print("Press Ctrl to start!")
    keyboard.wait("ctrl")
    EPF_start(__sleep__)
    time.sleep(__sleep__)
    EPFD_start(__sleep__)
    Process_Time = __sleep__ * 155 + (12 * __sleep__)
    print("Finished in ",Process_Time, "seconds")
    time.sleep(5)
    exit()


#.log file in nächster Version hinzufügen
#41x __sleep__
import time
from pynput.mouse import Button, Controller

mouse = Controller()

while(True):
    print ("Current position: " + str(mouse.position))
    time.sleep(0.5)
#The package pynput.mouse contains classes for monitoring and controlling the mouse
from pynput.mouse import Button, Controller

mouse = Controller()
print('The current mouse position is',format(mouse.position))


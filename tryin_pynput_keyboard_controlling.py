from pynput.keyboard import Controller, Key
import keyboard
import time
from ctypes import windll


""" k = Controller()
k.press(Key.cmd)
k.release(Key.cmd)
time.sleep(0.5)
k.press('c')
k.release('c')
time.sleep(0.5)
k.press(Key.enter)
k.release(Key.enter) """

wind11.user32.BlockInput(32)
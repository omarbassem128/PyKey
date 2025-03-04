from pynput.keyboard import Controller, Key
import time, keyboard

k = Controller()
keyboard.block_key() #figure out a way to use this function(block_key()) to block the entire keyboard during this code's execution
#Key.cmd is the windows key
k.press(Key.cmd)
k.release(Key.cmd)
time.sleep(0.5)
k.press('c')
k.release('c')
time.sleep(0.5)
k.press(Key.enter)
k.release(Key.enter)
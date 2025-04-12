from pynput import keyboard
import time

print('Program Is Running, enter ctrl+c to stop')


def on_press(key):
    try:
        print(f'{key} is pressed')
        time.sleep(2)
    except KeyboardInterrupt:
        print("Interrupt detected. exited gracefully")
    
        
        
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
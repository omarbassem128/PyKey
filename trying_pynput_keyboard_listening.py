from pynput import keyboard

print('Program Is Running')


def on_press(key):
    try:
        print(f'{key} is pressed')
    except AttributeError:
        print(f'Special Key:{key} is pressed')
        
        
with keyboard.Listener(on_press=on_press) as listener:
    listener.start()
    
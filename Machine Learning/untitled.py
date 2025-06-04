from pynput import keyboard

def on_press(key):
    try:
        print('Key pressed: {0}'.format(key.char))
    except AttributeError:
        print('Special key pressed: {0}'.format(key))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()




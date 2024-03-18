from pynput import keyboard
import pyautogui

def on_press(key):
    try:
        if key.char == 'k':
            print('Start')
            keyboard.Controller().press('c')

        if key.char == 'l':
            print('Stop')
            keyboard.Controller().release('c')

        if key.char == '=':
            return False

    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    try: 
        if key.char == 'l':
            # Stop listener
            print('Stop')
            keyboard.Controller.release('c')
        if key.char == '=':
            return False
    except:
        print('special key {0} pressed'.format(key))
        return True

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=None) as listener:
    listener.join()


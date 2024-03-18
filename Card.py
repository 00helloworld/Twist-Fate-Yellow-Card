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

        if key.char == 'e':
            keyboard.Controller().tap('w')
            for i in range(50):
                # a = time.time()
                # r,g,b = pyautogui.pixel(811, 1086)
                img = pyautogui.screenshot(region=(811, 1086, 1, 1))
                pxl = img.getpixel([0, 0])
                r, g, b = pxl[0], pxl[1], pxl[2]
                # print(time.time()-a)
                if r > 200 and g < 30 and b < 30:
                    print('Red')
                elif r > 200 and g > 200 and b < 20:
                    keyboard.Controller().tap('w')
                    print('Yellow')
                    break
                elif r < 65 and g < 65 and b > 150:
                    print('Blue')
                # time.sleep(0.05)

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


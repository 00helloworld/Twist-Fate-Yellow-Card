import pyautogui
import time

a = time.time()
img = pyautogui.screenshot(region=(785, 1060, 300, 400), imageFilename='/Users/dongyanshen/Desktop/DYSProjects/lol/tmp.png')
b = time.time()
img.save('/Users/dongyanshen/Desktop/DYSProjects/lol/tmp.png')  # region=(785, 1060, 52, 52) pix=(811, 1086, 1, 1)

print(b-a)
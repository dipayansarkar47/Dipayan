import pyautogui as pg
import time


time.sleep(10)

for i in range(1000):
    pg.write("You are under attack!")
    pg.press('enter')

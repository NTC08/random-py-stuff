import pyautogui as pyautogui
import keyboard
import time
import pywin32,win32con
import random
a = 0
b = 0
c = 0
d = 0
def click(x, y):
    pywin32.SetCursorPos((x, y))
    pywin32.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    #time.sleep(0.1) #This pauses the script for 0.1 seconds
    pywin32.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
while 1:
    if keyboard.is_pressed("q") == False:
        if pyautogui.locateOnScreen("sc.png", grayscale=True, confidence=0.6) != None:
            try:
                a, b, c, d = pyautogui.locateOnScreen("sc.png", grayscale=True, confidence=0.6)
                print(a,b,c,d)
                c = c / 2
                d = d / 2
                click(a + int(c), b + int(d))
            except:
               print("what")
               pass
               
        else:
            print("no")
            pass
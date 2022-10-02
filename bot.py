import pyautogui as pyautogui
import keyboard
import time
import win32api, win32con

#1 500 700
#2 600 700
#3 700 700
#4 800 700
time.sleep(1)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(500, 700)[1] == 0:
        click(510, 700)
    if pyautogui.pixel(600, 700)[0] == 0:
        click(610, 700)
    if pyautogui.pixel(700, 700)[0] == 0:
        click(710, 700)
    if pyautogui.pixel(800, 700)[0] == 0:
        click(810, 700)


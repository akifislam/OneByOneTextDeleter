import pyautogui
import time
import os

def play_alert_sound():
    os.system('afplay /System/Library/Sounds/Glass.aiff')

time_gap = 0.2


while(True):
    play_alert_sound()
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='right')
    # Press keyboard right,down,down,down,down
    time.sleep(time_gap)
    pyautogui.press('down')
    
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down') 
    
    time.sleep(time_gap)
    pyautogui.press('enter')
    time.sleep(time_gap)    
    pyautogui.press('tab')
    time.sleep(time_gap)
    pyautogui.press('enter')
    time.sleep(1)

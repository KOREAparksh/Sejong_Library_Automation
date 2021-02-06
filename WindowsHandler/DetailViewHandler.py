import pyautogui
import time

def selectRelationTab(w) :
    w_width = w[0].size.width
    w_height = w[0].size.height
    start_x = w[0].left
    start_y = w[0].top
    region = (start_x,int(w_height/2), int(w_width/2), int(w_height/2))
    for i in pyautogui.locateAllOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/relationIngoIcon.png", confidence = 0.8, region = region):
        pyautogui.moveTo(i)
        pyautogui.move(50,0)
        pyautogui.click()
    
    return

def checkAlreadyHave(w) :
    time.sleep(0.25)
    w_width = w[0].size.width
    w_height = w[0].size.height
    start_x = w[0].left
    start_y = w[0].top
    
    if pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/NoneIntroTable.png") :
        return False
    else :
        return True
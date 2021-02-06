import pyautogui
import time

def findRegistNumberCategory():
    w = pyautogui.getWindowsWithTitle("통합작업환경")
    region = (w[0].left+20, w[0].top+20, int(w[0].size.width/4), int(w[0].size.height/4))
    
    categoryBox = pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/categoryEssentialInitName.png"
                                             , confidence = 0.9
                                             , region = region )
    if categoryBox is None :
        pyautogui.click(pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/categoryExpander.png"
                                                , confidence = 0.9
                                                , region =region))
        pyautogui.move(0,200)
        while True :
            time.sleep(0.1)
            categoryBox = pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/categoryEssentialInitName.png"
                                                , confidence = 0.9
                                                , region = region)
            if categoryBox is not None :
                break
            pyautogui.scroll(500)
    return categoryBox

def putsRegistNumber(registNumberString) :
    categoryBox = findRegistNumberCategory()
    
    pyautogui.click(categoryBox)
    
    pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("back")
    pyautogui.typewrite(registNumberString)
    pyautogui.press("enter")
    return


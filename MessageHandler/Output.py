import pyautogui

def checkBeforeTheRunning(start, end) :
    msg = str(start) + " ~ " + str(end)
    
    result = pyautogui.confirm("아래의 등록번호가 맞으면 \"예\"를 눌러주세요. \n" + msg, "등록번호 확인")
    
    return result

def alertInvalidRange() :
    pyautogui.alert("끝번호가 시작번호보다 작습니다.\n다시 입력하세요.")
    return 
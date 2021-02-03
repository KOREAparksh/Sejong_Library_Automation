import pyautogui

def getStartRegistNumber() :
    result = pyautogui.prompt("작업할 등록번호 범위의 시작번호를 입력하세요.\n 등록번호는 앞\"0\" 6개, 등록번호 6개입니다."
                              ,"등록번호 시작번호 입력")
    
    
    return result

def getEndRegistNumber() :
    result = pyautogui.prompt("작업할 등록번호 범위의 끝번호를 입력하세요.\n 등록번호는 앞\"0\" 6개, 등록번호 6개입니다."
                              ,"등록번호 끝번호 입력")
    
    
    return result

#print(getStartRegistNumber())
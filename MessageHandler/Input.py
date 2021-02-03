import pyautogui

def isValidNumber(number) :
    if  len(str(number)) is not 12 :
        raise ValueError
    
    
    
    return 

def getStartRegistNumber() :
    msg = None
    while True : 
        result = pyautogui.prompt("작업할 등록번호 범위의 시작번호 12자리를 입력하세요.\n 등록번호는 앞\"0\" 6개, 등록번호 6개입니다."
                                ,"등록번호 시작번호 입력", msg)
        if result is None :
            return
        
        try :
            isValidNumber(result)
            return result
        except :
            msg = "등록번호를 정확히 입력하세요"
            continue
    

def getEndRegistNumber() :
    msg = None
    while True : 
        result = pyautogui.prompt("작업할 등록번호 범위의 끝번호 12자리를 입력하세요.\n 등록번호는 앞\"0\" 6개, 등록번호 6개입니다."
                              ,"등록번호 끝번호 입력", msg)
        if result is None :
            return
        
        try :
            isValidNumber(result)
            return result
        except :
            msg = "등록번호를 정확히 입력하세요"
            continue

print(getStartRegistNumber())
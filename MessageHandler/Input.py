import pyautogui

def isValidNumber(number) :
    if  len(str(number)) is not 12 :
        raise ValueError
    
    
    
    return 

def getStartRegistNumber() :
    return inputRegistNummber("시작번호")
    

def getEndRegistNumber() :
    return inputRegistNummber("끝번호")

def inputRegistNummber(position):
    msg = None
    while True : 
        result = pyautogui.prompt("작업할 등록번호 범위의 {} 12자리를 입력하세요.\n 등록번호는 앞\"0\" 6개, 등록번호 6개입니다.".format(position)
                                  ,"등록번호 {} 입력".format(position), msg)
        if result is None :
            return result
        
        try :
            isValidNumber(result)
            return result
        except :
            msg = "등록번호를 정확히 입력하세요"
            continue

print(getStartRegistNumber())
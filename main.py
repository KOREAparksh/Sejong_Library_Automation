import MessageHandler.Input as input
import MessageHandler.Output as output
import sys

def isValidRange(start, end) :
    if int(start) > int(end) :
        output.alertInvalidRange()
        return False
    return True

########################

startNumber = 0
endNumber = 0

#########################main start point

#등록번호 입력
while True : 
    startNumber = input.getStartRegistNumber()
    if startNumber is None :
        sys.exit()
    
    endNumber = input.getEndRegistNumber()
    if endNumber is None :
        sys.exit()
    
    if isValidRange(startNumber[6:12], endNumber[6:12]) :
        break

#등록번호 확인
if output.confirmBeforeTheRunning(startNumber, endNumber) == "Cancel" : 
    sys.exit()
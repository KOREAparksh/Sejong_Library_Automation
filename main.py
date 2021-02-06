import MessageHandler.Input as input
import MessageHandler.Output as output
import WindowsHandler.FindBooks as findBooks
import pyautogui
import sys

def isValidRange(start, end) :
    if int(start) > int(end) :
        output.alertInvalidRange()
        return False
    return True

########################

startNumber = 0
endNumber = 0
registNumberString = ""                                                   #등록번호 입력에 쓰일 문자열

#########################main start point

#창 활성화 확인
w = pyautogui.getWindowsWithTitle("통합작업환경")

if len(w) == 0 :
    output.sendAlertMessage("통합작업환경(IWS)를 열고 실행해주세요.")
    sys.exit()

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
registNumberString = str(startNumber) + " ~ " + str(endNumber)

if output.confirmBeforeTheRunning(registNumberString) == "Cancel" : 
    sys.exit()

#등록번호 검색
findBooks.putsRegistNumber(registNumberString)

#체크박스 선택

#상세보기 진입

#창크기 추출

#관계정보 탭 선택 (1회)

#이미 초록목차가 작성된 책인지 확인

#ISBN 추출

#초록목차 크롤링

#초록목차 저장
import MessageHandler.Input as input
import MessageHandler.Output as output
import WindowsHandler.FindBooks as findBooks
import WindowsHandler.DetailViewHandler as detailHandler
import pyautogui
import time
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
time.sleep(2)
findBooks.selectCheckBox(int(endNumber) - int(startNumber)) 

#상세보기 진입
pyautogui.move(200, 0)
pyautogui.rightClick() 
time.sleep(0.3)
pyautogui.rightClick() 
time.sleep(0.3)
pyautogui.press("down")
pyautogui.press("enter")

#관계정보 탭 선택 (1회)
time.sleep(1.5)
detailHandler.selectRelationTab(w)

#창크기 추출
w_width = w[0].size.width
w_height = w[0].size.height
start_x = w[0].left
start_y = w[0].top

#저장시스템
count = int(endNumber) - int(startNumber)
now_count = 0

while now_count < count :
    
    now_count += 1
    #이미 초록목차가 작성된 책인지 확인
    if detailHandler.checkAlreadyHave(w) :
        continue

    #ISBN 추출

    #초록목차 크롤링

    #초록목차 저장
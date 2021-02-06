import MessageHandler.Input as input
import MessageHandler.Output as output
import WindowsHandler.FindBooks as findBooks
import WindowsHandler.DetailViewHandler as detailHandler
import WebCrawling.WebCrawling as WebCrawling
import pyautogui
import pyperclip
import time
import sys

def isValidRange(start, end) :
    if int(start) > int(end) :
        output.alertInvalidRange()
        return False
    return True

def pushNextButton() :
    region = (start_x + w_width//2, start_y+30, w_width//2, w_height//2)
    pyautogui.click(pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/nextButton.png"
                                                , region = region))

def checkLastBook() :
    if pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/nextButton_grayscale.png") :
        output.sendAlertMessage("끝났습니다!")
        sys.exit()
    return
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
center_x = w[0].center.x
center_y = w[0].center.y
browser = WebCrawling.initBrowser()

while now_count < count :
    
    now_count += 1
    #이미 초록목차가 작성된 책인지 확인
    if detailHandler.checkAlreadyHave(w) :
        checkLastBook()
        pushNextButton()
        continue

    #ISBN 추출
    time.sleep(0.4)
    pyautogui.click(center_x+100, center_y, clicks=2, interval=0.2)
    
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")

    isbn = pyperclip.paste()
    index = isbn.find("▼a")
    index+=2
    isbn = isbn[index : index + 13]

    #초록목차 크롤링
    bookIntro, tableContent = WebCrawling.getData(browser, isbn)

    #초록목차 저장
    detailHandler.saveInformation(bookIntro, tableContent, w)
    
    #버튼 비활성화 되면 끝남.
    checkLastBook()
    pushNextButton()
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

def initOptions() :
    # 옵션 생성
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("headless")                                           # 창 숨기는 옵션 추가
    return options

def initBrowser():
    options = initOptions()
    browser = webdriver.Chrome("C:/Program Files (x86)/Sejong Library Automation/driver/chromedriver.exe", options=options)
    return browser

def expandDisplay(browser) :
    #초록
    elem = browser.find_element_by_xpath(".//*[@id='bookIntroOpen']/..")
    if elem.get_attribute("style") == "display: block;" :
        elem = browser.find_element_by_id("bookIntroOpen")
        elem.click()
    
    #목차
    elem = browser.find_element_by_xpath(".//*[@id='tableOfContentsOpen']/..")
    if elem.get_attribute("style") == "display: block;" :
        elem = browser.find_element_by_id("tableOfContentsOpen")
        elem.click()
    return browser

def getBookDetailUrl(registNumber) :
    url  = "https://book.naver.com/search/search.nhn?&query="
    url = url + str(registNumber)
    print(url)
    
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    try :
        bidUrl = soup.find("ul", attrs = {"id" : "searchBiblioList"})
        return bidUrl.find("a")["href"]
    except AttributeError :
        return None


def getData(browser, registNumber) :
    url = getBookDetailUrl(registNumber) 
    if url is None :
        return None
    
    browser.get(url)
    expandDisplay(browser)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    
    try :
        bookIntro =  soup.find("div", attrs = {"id" : "bookIntroContent"})
        bookIntro = bookIntro.get_text()
    except :
        bookIntro = ""
    try :
        tableOfContents =  soup.find("div", attrs = {"id" : "tableOfContentsContent"})
        tableOfContents = tableOfContents.get_text()
    except :   
        tableOfContents = ""
        
    return bookIntro, tableOfContents

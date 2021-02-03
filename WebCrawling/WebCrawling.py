from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests 
import re
from bs4 import BeautifulSoup
import time

def initOptions() :
    # 옵션 생성
    options = webdriver.ChromeOptions()
    options.add_argument("headless")                                           # 창 숨기는 옵션 추가
    return options

def initBrowser():
    options = initOptions()
    browser = webdriver.Chrome("./chromedriver", options=options)
    return browser


def enterURL(browser,url) :
    #url = "https://book.naver.com/bookdb/book_detail.nhn?bid=16852884"        #펼쳐야하는거
    #url = "https://book.naver.com/bookdb/book_detail.nhn?bid=17726967"        #둘다 안펼쳐도 되는거
    browser.get(url) 
    return

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



def getData() :
    browser = initBrowser()
    url = "https://book.naver.com/bookdb/book_detail.nhn?bid=16852884" #펼쳐야하는거
    enterURL(browser, url)
    
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    
    bookIntro =  soup.find("div", attrs = {"id" : "bookIntroContent"})
    #print(bookIntro.get_text())
    tableOfContents =  soup.find("div", attrs = {"id" : "tableOfContentsContent"})
    #print(tableOfContents.get_text())
    
    browser.quit()
    
    return bookIntro.get_text(), tableOfContents.get_text()

import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

def ftlGenerator():
    driver = webdriver.Chrome(options=options, executable_path='../chromedriver')
    driver.get('https://www.footlocker.com')
    while driver != webdriver.Chrome(options=options, executable_path='../chromedriver'):
        print('Generating...')
        savedCookies = open('cookies.txt', 'a') 
        cookie = driver.get_cookie('_abck')
        print(cookie['value'], file = savedCookies) 
        print(cookie['value'])
        time.sleep(1)
        driver.delete_cookie('_abck')
        time.sleep(2)
        driver.refresh()
        time.sleep(2)

def eastbayGenerator():
    driver = webdriver.Chrome(options=options, executable_path='../chromedriver')
    driver.get('https://www.eastbay.com')
    while driver != webdriver.Chrome(options=options, executable_path='../chromedriver'):
        print('Generating...')
        savedCookies = open('cookies.txt', 'a') 
        cookie = driver.get_cookie('_abck')
        print(cookie['value'], file = savedCookies) 
        print(cookie['value'])
        time.sleep(1)
        driver.delete_cookie('_abck')
        time.sleep(2)
        driver.refresh()
        time.sleep(2)

def champsGenerator():
    driver = webdriver.Chrome(options=options, executable_path='../chromedriver')
    driver.get('https://www.champs.com')
    while driver != webdriver.Chrome(options=options, executable_path='../chromedriver'):
        print('Generating...')
        savedCookies = open('cookies.txt', 'a') 
        cookie = driver.get_cookie('_abck')
        print(cookie['value'], file = savedCookies) 
        print(cookie['value'])
        time.sleep(1)
        driver.delete_cookie('_abck')
        time.sleep(2)
        driver.refresh()
        time.sleep(2)

def ftaGenerator():
    driver = webdriver.Chrome(options=options, executable_path='../chromedriver')
    driver.get('https://www.footaction.com')
    while driver != webdriver.Chrome(options=options, executable_path='../chromedriver'):
        print('Generating...')
        savedCookies = open('cookies.txt', 'a') 
        cookie = driver.get_cookie('_abck')
        print(cookie['value'], file = savedCookies) 
        print(cookie['value'])
        time.sleep(1)
        driver.delete_cookie('_abck')
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
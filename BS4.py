from bs4 import BeautifulSoup as bs
import time
from bs4 import*
import requests
import re
from requests import Session
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Chrome('/usr/bin/chromedriver')
headers = {'accept':'*/*',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

url = 'https://www.redbubble.com/shop/bees?ref=search_box'
session = requests.Session()
response = session.get(url, headers=headers)
soup = bs(response.content, 'html.parser')






def parce(url, headers):

    finda = soup.findAll('a', {'class':'styles__normalLink--2LmvE'})
    container = [] #убирая код связанный контейнером вытаскиваем все из списка если нам это нужно
    for link in soup.findAll("a", {'class':'styles__normalLink--2LmvE'}):
        enden_urls =  'https://www.redbubble.com' + link.get("href")
        container.append(enden_urls)
    return container

def find_image(url, headers):

    find = soup.findAll('img', {'class':'default__image--2pxkw styles__image--2yCHr'})
    print(find)
    return find


def find_from_title_png(url, headers):
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    images = driver.find_elements_by_xpath('.//img[contains(@class, "styles__image--2CwxX styles__image--2yCHr")][@srcset]')

    print(images)
    # for link2 in images:
    #     new_link = link2.get('src')
    #     print(new_link)






find_from_title_png(url, headers)

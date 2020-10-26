from bs4 import BeautifulSoup as bs
import time
from bs4 import*
import requests
import re
from requests import Session
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import Workbook, load_workbook

wb = load_workbook('43.xlsx')
sheet_range = wb.worksheets[0]
container = []

for parce in sheet_range['A1':'A10']:
    for cell in parce:
        print(cell.value)
        if cell.value == None:
            break
        container.append(cell.value)

print(container)
driver = webdriver.Chrome('driver/chromedriver')
headers = {'accept':'*/*',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
url = 'http://gippokrat.kz/catalog/?query='
session = requests.Session()
response = session.get(url, headers=headers)
soup = bs(response.content, 'html.parser')
options = webdriver.ChromeOptions()
options.add_argument('headless')


cont = []

def gippo(container):
    for i in container:
        url2 = 'http://gippokrat.kz/catalog/?query=' + i
        driver.get(url2)
        try:
            price = driver.find_element_by_class_name('items__price').text
        except:
            print('не найден препарат ' + i)
        reg = re.findall(r'\d+', price)
        if len(reg) >= 2:
            print("bad")
            new_massive = reg[0] + reg[1]
            cont.append(new_massive)
            continue
        print(reg)
        cont.append(reg[0])
    driver.close()
    return cont

gippo(container)
print(cont)

case = []
for i in cont:
    case.append(int(i))

print(sum(case))

# def parce(url, headers):
#
#     finda = soup.findAll('p', {'class':'items__price'})
#     container = [] #убирая код связанный контейнером вытаскиваем все из списка если нам это нужно
#     for link in soup.findAll("a", {'class':'styles__normalLink--2LmvE'}):
#         enden_urls =  'https://www.redbubble.com' + link.get("href")
#         container.append(enden_urls)
#     return container
#
# def find_image(url, headers):
#
#     find = soup.findAll('img', {'class':'default__image--2pxkw styles__image--2yCHr'})
#     print(find)
#     return find
#
#
# def find_from_title_png(url, headers):
#     driver.get(url)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     images = driver.find_elements_by_xpath('.//img[contains(@class, "styles__image--2CwxX styles__image--2yCHr")][@srcset]')
#
#     print(images)
#     # for link2 in images:
#     #     new_link = link2.get('src')
#     #     print(new_link)


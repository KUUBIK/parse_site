from bs4 import BeautifulSoup as bs
from bs4 import*
import requests
import re
from requests import Session

headers = {'accept':'*/*',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

url = 'https://www.redbubble.com/shop/stickers?ref=global-nav-top'
def parce(url, headers):

    session = requests.Session()
    response = session.get(url, headers = headers)
    soup = bs(response.content, 'html.parser')
    finda = soup.findAll('a', {'class':'styles__normalLink--2LmvE'})
    for image in finda:
        urls = image['href']
        url = 'https://www.redbubble.com' + urls
        print(url)
parce(url, headers)

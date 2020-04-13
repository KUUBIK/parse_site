from bs4 import BeautifulSoup as bs
from bs4 import*
import requests
import re
from requests import Session

headers = {'accept':'*/*',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

url = 'https://www.redbubble.com/people/cheezup/works/11591345-hammerhead-shark?cat_context=u-stationery&grid_pos=108&p=sticker&rbs=811a85d8-4ba6-4074-80e3-8a2698f35f45&ref=shop_'
def parce(url, headers):

    session = requests.Session()
    response = session.get(url, headers = headers)
    soup = bs(response.content, 'html.parser')
    finda = soup.findAll('img', {'class':'GalleryImage__img--12Vov'})
    for image in finda:
        print(image['src'])


parce(url, headers)

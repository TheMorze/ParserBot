import requests
from bs4 import BeautifulSoup

# URL, по которому осуществляются запросы
URL = 'https://sport24.ru/football'

def extract_from_sport24():
    request = requests.get(url=URL)
    soup = BeautifulSoup(request.text, 'html.parser')
    
    news = soup.find('div', {'class': 'desktop-order-2'})
    print(news)

extract_from_sport24()
from aiogram import Bot
import asyncio

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

from lexicon.lexicon import LEXICON_NEWSLETTER
from database.service import Database

# URL, по которому осуществляются запросы
URL = 'https://www.sports.ru/football/'

def extract_from_sports():
    
    request = requests.get(url=URL)
    soup = BeautifulSoup(request.text, 'html.parser')
    
    main_news = soup.find('section', {'class': 'aside-news-block analyticsTrackView'})
    last_news = main_news.find_all('li')[0]
    
    a = last_news.find('a')
    
    title = a.text
    link = a['href']
    time = last_news.find('time')['datetime']
    source = 'sports.ru'
    
    result = {'title': title, 'link': link, 'time': time, 'source': source}
    
    if is_fresh(result):
        return result

def is_fresh(news):
    d = datetime.strptime(news['time'], '%Y-%m-%d %H:%M:%S')
    
    news_time = d.timestamp()
    now = datetime.today().timestamp()
    
    # Разница во времени в минутах
    td = (now - news_time) // 60
    
    return td <= 60
    
news = extract_from_sports()

async def check_sports_ru(bot: Bot):
    
    while True:
        news = extract_from_sports()
        if news:
            user_ids = Database.get_users_newsletter()
            
            for user_id in user_ids:
                last_news = Database.get_last_news(user_id=user_id)
                if last_news != news['link']:
                    Database.set_last_news(user_id=user_id, link=news['link'])
                    first_name = Database.get_first_name(user_id=user_id)
                    await bot.send_message(chat_id=user_id,
                                           text=LEXICON_NEWSLETTER['news'].format(
                                                first_name=first_name,
                                                source=news['source'],                                                             title=news['title'],
                                                link=news['link'],
                                                time=news['time'])
                                           )
                
        await asyncio.sleep(60)
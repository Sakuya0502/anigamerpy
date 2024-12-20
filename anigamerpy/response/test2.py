'''
from botdata import anime

anigamer = anime.anigamer().search_anime('bang')
print(anigamer)

'''
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}
r = requests.get('https://ani.gamer.com.tw/search.php?keyword=overlord', headers=headers)
if r.status_code == 200:
    anime_list = []
    soup = BeautifulSoup(r.text, 'html.parser')
    newanime_item = soup.select_one('.animate-theme-list > .theme-list-block')
    anime_items = newanime_item.select('.theme-list-main')
    for anime_item in anime_items:
        anime_name = anime_item.select_one('.theme-name').text.strip()
        print(anime_name)
        anime_watch_number = anime_item.select_one('.show-view-number > p').text.strip()
        print(anime_watch_number)
        anime_episode = anime_item.select_one('.theme-number').text.strip()
        print(anime_episode)
        anime_year = anime_item.select_one('.theme-time').text.strip()
        print(anime_year)
        anime_href = anime_item.get('href')
        print('https://ani.gamer.com.tw/' + anime_href)
        anime_pic = anime_item.select_one('.theme-img')['data-src']
        print(anime_pic)
        print('----------------')
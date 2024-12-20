from bs4 import BeautifulSoup
import requests

from .error import ErrorType

class Search:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
        }
        self.base_url = 'https://ani.gamer.com.tw/search.php?keyword='
        self.result = []
        self.search_data = {}
    
    def search_anime(self, keyword: str):
        req = requests.get(self.base_url + keyword, headers=self.headers)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, 'html.parser')
            search_anime_item = soup.select_one('.animate-theme-list > .theme-list-block')
            search_items = search_anime_item.select('.theme-list-main')
            for search_item in search_items:
                anime_name = search_item.select_one('.theme-name').text.strip()
                anime_watch_number = search_item.select_one('.show-view-number > p').text.strip()
                anime_episode = search_item.select_one('.theme-number').text.strip()
                anime_year = search_item.select_one('.theme-time').text.strip()
                anime_href = search_item.get('href')
                anime_pic = search_item.select_one('.theme-img')['data-src']
                self.sdata = {
                    'name': anime_name,
                    'watch_count': anime_watch_number,
                    'episode': anime_episode,
                    'years': anime_year,
                    'href': anime_href,
                    'image': anime_pic
                }
                self.result.append(self.sdata)
                self.search_data = {}
            if anime_name == '':
                return ErrorType.no_result()
        else:
            return ErrorType.status_error(str(req.status_code))
        return self.result
    
class SearchResponse:
    def __init__(self, keyword: str):
        self.data = Search().search_anime(keyword=keyword)
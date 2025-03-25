from .response import searchanime, newanime, allanime

class Anime:
    def __init__(self):
        pass

    def search_anime(self, keyword: str):
        return searchanime.SearchResponse(keyword=keyword)
    
    def new_anime(self):
        return newanime.NewAnimeResponse()
    
    def all_anime(self, tags:list = [], category:int = None, target:int = None, sort:int = None, page:int = None):
        return allanime.AllAnimeResponse(tags=tags, category=category, target=target, sort=sort, page=page)
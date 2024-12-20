from .response import searchanime, newanime

class Anime:
    def __init__(self):
        pass

    def search_anime(self, keyword: str):
        return searchanime.SearchResponse(keyword=keyword)
    
    def new_anime(self):
        return newanime.NewAnimeResponse()
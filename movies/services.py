import requests
from django.conf import settings

class TMDBService:
    BASE_URL = "https://api.themoviedb.org/3"

    @classmethod
    def search_movie(cls, title):
        if not getattr(settings, 'TMDB_API_KEY', None):
            return None

        url = f"{cls.BASE_URL}/search/movie"
        params = {
            'api_key': settings.TMDB_API_KEY,
            'query': title,
            'language': 'en-US'
        }

        try:
            response = requests.get(url, params=params, timeout=5)
            data = response.json()

            if data.get('results'):
                movie = data['results'][0]
                return {
                    'tmdb_id': str(movie['id']),
                    'poster_path': f"https://image.tmdb.org/t/p/w500{movie.get('poster_path', '')}",
                    'overview': movie.get('overview', '')[:500],
                    'release_date': movie.get('release_date'),
                    'tmdb_rating': movie.get('vote_average', 0)
                }
        except:
            pass
        return None

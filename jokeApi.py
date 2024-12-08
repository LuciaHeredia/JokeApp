import requests

api_url = 'https://v2.jokeapi.dev/joke/Programming?type=single' # category: Programming

def get_joke():
    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return e
    
    data = response.json()
    return data['joke']


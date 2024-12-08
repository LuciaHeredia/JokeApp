import requests

joke_category = 'Programming'
joke_type='single'
api_url = 'https://v2.jokeapi.dev/joke/'+joke_category+'?type='+joke_type

def get_joke_category():
    return joke_category

def get_joke():
    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return e
    
    data = response.json()
    return data['joke']


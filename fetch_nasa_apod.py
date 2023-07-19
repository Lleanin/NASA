import requests
import os
from save_tools import save_picture,get_extension

from dotenv import load_dotenv


def main():
    load_dotenv()
    nasa_token = os.getenv("NASA_API_TOKEN")
    
    payload ={"count" : 30,
              "api_key" : nasa_token
             }
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    filename = 'NASA_'

    for index, api_response in enumerate(response.json(),1):
        url = api_response['url']
        extension = get_extension(url)
        if extension:
            full_name = f'{filename}{index}{extension}'
            save_picture(url, full_name)

    
if __name__ == '__main__':
    main()
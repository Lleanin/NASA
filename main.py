import random
import os
from pathlib import Path

import requests
from urllib.parse import urlparse


def fetch_spacex_last_launch():
    id = '5eb87d42ffd86e000604b384'
    url = 'https://api.spacexdata.com/v5/launches/{}'.format(id)
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    filename = 'spaceX_'
    for index,picture in enumerate(links,1):
        full_name = f'{filename}{index}.jpg'
        save_picture(picture, full_name)


def save_picture(url, filename, api_key=''):
    response = requests.get(url, params = api_key)
    response.raise_for_status()
    full_name = os.path.join('images', filename)
    with open(full_name, 'wb') as file:
            file.write(response.content)


def get_extension(url):
    path = urlparse(url).path
    return os.path.splitext(path)[1]


def fetch_nasa_apod():

    payload ={"count" : 30,
              "api_key" : "OMDiuXqrX2a1MlYjDYW0pWoHgoU2duOwanEDIcbQ"
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
    

def fetch_epic_photo():
    payload = {"api_key" : "OMDiuXqrX2a1MlYjDYW0pWoHgoU2duOwanEDIcbQ"}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params = payload)
    response.raise_for_status()

    epic_photos = random.randint(5, 10)
    for index in range(epic_photos):
        file_name = f'epic_{index+1}.png'
        data = response.json()[index]
        date = data['date'].split()[0]
        date = date.split('-')
        name = data['image']
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{name}.png'
        save_picture(epic_image_url, file_name, payload)
    

def main():
    Path("images/").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()
    fetch_nasa_apod()
    fetch_epic_photo()


if __name__ == '__main__':
    main()
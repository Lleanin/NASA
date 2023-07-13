import os
from pathlib import Path

import requests
from urllib.parse import urlparse


def save_picture(url, filename, api_key=''):
    Path("images/").mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params = api_key)
    response.raise_for_status()
    full_name = os.path.join('images', filename)
    with open(full_name, 'wb') as file:
            file.write(response.content)


def get_extension(url):
    path = urlparse(url).path
    return os.path.splitext(path)[1]


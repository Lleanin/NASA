import argparse
import os
import random

from dotenv import load_dotenv
import requests

from save_tools import save_picture


def main():
    load_dotenv()
    nasa_token = os.environ.get("NASA_API_TOKEN")

    parser = argparse.ArgumentParser(description='Данный файл скачивает фотографии с последнего запуска')
    parser.add_argument('--folder',
                        type=str,
                        default='folder',
                        help='Введите название папки')

    args = parser.parse_args()
    folder = args.folder

    payload = {"api_key": nasa_token}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=payload)
    response.raise_for_status()

    for index in range(random.randint(5, 10)):
        file_name = f'epic_{index+1}.png'
        nasa_epic_data = response.json()[index]
        date = nasa_epic_data['date'].split()[0]
        date = date.split('-')
        name = nasa_epic_data['image']
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{name}.png'
        save_picture(folder, epic_image_url, file_name, payload)


if __name__ == '__main__':
    main()

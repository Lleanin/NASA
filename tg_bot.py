import os
import random
import time

import argparse
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.getenv("TG_TOKEN")

    bot = telegram.Bot(token=tg_token)

    parser = argparse.ArgumentParser(description='Данный файл отправляет случайные фотографии')
    parser.add_argument('--time', 
                        type=int,
                        default=14400, 
                        help='Введите с какой переодичностью отправлят картинки'
                        )
    args = parser.parse_args()
    periodicity = args.time

    while True:
        all_files = os.walk("images")
        for array_of_files in all_files:
            folder, nested_folder, files_names = array_of_files
            filename = random.choice(files_names)
        full_name = os.path.join(folder, filename)
        bot.send_document(chat_id='@nasa_apishka', document=open(full_name, 'rb'))
        time.sleep(periodicity)


if __name__ == '__main__':
    main()
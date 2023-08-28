import os
import random
import time

import argparse
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.getenv("TG_TOKEN")
    tg_chat_id = os.getenv("TG_CHAT_ID")

    bot = telegram.Bot(token=tg_token)

    parser = argparse.ArgumentParser(description='Данный файл отправляет случайные фотографии')
    parser.add_argument('--time',
                        type=int,
                        default=14400,
                        help='Введите с какой переодичностью отправлят картинки'
                        )
    parser.add_argument('--folder',
                        type=str,
                        default='folder',
                        help='Введите название папки')
    args = parser.parse_args()
    folder = args.folder
    periodicity = args.time

    while True:
        all_files = os.walk(folder)
        for array_of_files in all_files:
            folder, nested_folder, files_names = array_of_files
            filename = random.choice(files_names)
            full_name = os.path.join(folder, filename)
            file = open(full_name, 'rb')
            with file:
                bot.send_document(chat_id=tg_chat_id, document=file)
            time.sleep(periodicity)


if __name__ == '__main__':
    main()

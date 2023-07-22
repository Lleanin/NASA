import os
import telegram

tg_token = os.getenv("TG_TOKEN")
bot = telegram.Bot(token="6137754993:AAGRGpMcgxFMmt27AYjIi2vqa7SvuN7mRQk")

bot.send_message(chat_id='@nasa_apishka', text="I'm sorry Dave I'm afraid I can't do that.")

print(bot.get_me())
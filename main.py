import io

import  telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests

TOKEN = "5810449448:AAHiFZR1N-ZaXZ3Ipa9GKseAeal-E9NQeig"

bot = telebot.TeleBot(token=TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def welcome_message(message):
    welcome_message = "Привет. Этот бот достает фотки кошек из интернета!"

    bot.reply_to(message, welcome_message, reply_markup=keyboard())


@bot.message_handler(content_types=['text'])
def message_handler(message):
    if message.text == "Дай кота!":
        cat = get_cat()
        bot.send_photo(message.chat.id, cat)


def keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton("Дай кота!")
    keyboard.add(button)

    return keyboard


def get_cat():

    headers = {"contact-type": "image/jpeg"}
    reply = requests.get("https://thiscatdoesnotexist.com/", headers=headers)

    image = reply.content
    image = io.BytesIO(image)

    return image


bot.infinity_polling()
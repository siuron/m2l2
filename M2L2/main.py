import telebot
import os
import random

print(os.listdir('images'))
bot = telebot.TeleBot("8122935038:AAFOtV7uLe5J-Xao5ussiXjE9Ap0PeaC7dc")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот который тебе поможет сохранить природу")

@bot.message_handler(commands=['and?'])
def send_hello(message):
    bot.reply_to(message, "тебе нужно не кидать мусор по сторонам?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "надеюсь ты понял что нудно делать!")


@bot.message_handler(commands=['mem'])
def send_mem(message):
    images = os.listdir("images")
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)    

bot.polling()
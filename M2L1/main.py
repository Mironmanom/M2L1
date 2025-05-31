import telebot
import os
import random
bot = telebot.TeleBot("Token")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    mimages = os.listdir('imagesmem')
    mimage = random.choice(mimages)
    with open(f'images/{mimage}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)     
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

 
    
bot.polling()

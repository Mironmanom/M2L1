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
    a = random.randint(1,100)
    if a == 1:
        images = os.listdir('images')
        image = random.choice(images)
        with open(f'images3/{image}', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    if a >= 2 and a < 50:
        images = os.listdir('images2')
        image = random.choice(images)
        with open(f'images2/{image}', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    if a >=50 :
        images = os.listdir('images1')
        image = random.choice(images)
        with open(f'images1/{image}', 'rb') as f:  
            bot.send_photo(message.chat.id, f)     
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

 
    
bot.polling()
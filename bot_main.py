from telebot import TeleBot, types
import csv
import shutil
import time
import os
from  bot_functions import *
verjin = 1
bot = TeleBot("5417482315:AAFGZylYj-w6Ev8n03ikJRECYh71pCa9Q8k")

@bot.message_handler(commands=['start'])
def start(message):
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    show_button = types.KeyboardButton("Show new data")
    mark.add(show_button)
    bot.send_message(message.chat.id, f"Hii {message.from_user.first_name}", reply_markup=mark) 
    get_chat_id(message) #----------------------------------------------------------------------get chat id---------------------------
   
@bot.message_handler(content_types=["text"])
def update(message):
    global verjin
    if message.text.lower() in ["new" ,"new data", "show", "/show","show new data", "/show new data"]:
        with open("names.csv", "r") as names_file:
            names_iter = names_file.readlines()
            while verjin < len(names_iter):
                name_list = names_iter[verjin].split(",")
                (first_name, last_name,insta_nik, phone, email, sex, hms, ymm) = name_list    
                mess = "_"*22 + f"\nFirst name: {first_name}\nLast name: {last_name}\nPhone: {phone}\nEmail: {email}\nSex: {sex}\nTime of registration։ {hms} {ymm}\n" + "_"*22
                # print(insta_nik)
                try:
                    img = get_profil_pic(insta_nik)
                    bot.send_photo(message.chat.id,photo=img, caption=mess)
                    shutil.rmtree(insta_nik)
                except:
                    bot.send_message(message.chat.id,mess)    
                verjin += 1          
            else:
                # print("="*50)
                del_data_in_file()
                bot.send_message(message.chat.id, "No new data.")
                verjin = 1
    elif message.text.lower() in ["add", "add new name"]:
        add_name(["first_name","last name","___.lilit.____", "phone", "email", "sex"])
    else:
        os.system("clear||cls")
        bot.send_message(message.chat.id, "/start")
bot.polling(none_stop=True)
import time
import os
import instaloader
from telebot import TeleBot
import shutil
import pymysql as MySQLdb

def get_chat_id(message):
    with open("ids.txt", "a") as id_file:
        id_file.write(f"{message.chat.id}\n")

def get_profil_pic(insta_nik: str):
    ig = instaloader.Instaloader()
    ig.download_profile(profile_name=insta_nik, profile_pic_only=True)
    for img in os.listdir(insta_nik):
        if "profile_pic.jpg" in img:
            return open(insta_nik +"/"+ img, "rb")

def loc_time():
    ymm = f"{time.localtime().tm_mday}:{time.localtime().tm_mon}:{time.localtime().tm_year}"
    hms = f"{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}"
    return(hms, ymm)

def get_info(minute: int, host, user, password, db):

    db = MySQLdb.connect(host=host, user=user, password=password, db=db)
    cursor = db.cursor()
    cursor.execute(f"select * from verif_date where verif_date.Date >= (now() - interval {minute}  minute)")
    data = cursor.fetchall()
    db.close()
    return data

def start_procesing(bot: TeleBot, minute, host, user, password, db, channel_id):
    bot.send_message(chat_id = channel_id,text =  "OOOOOOOOOO" )
    
    # data_file  = get_info(minute = minute, host = host, user = user, password = password, db = db)
    # if len(data_file) == 0:
    #     bot.send_message(channel_id, f"No new data. {loc_time()}")
    # else:
    #     for info in  data_file:
    #         idd, date_time, status, name, surname, tel, email, date_birtf, sex, soc_link = info
    #         soc_link = "https://www.instagram.com/bagrat_51"

    #         insta_nik = soc_link[26:] if "https://www.instagram.com/" in soc_link else "No insta-link"
                
    #         mess = "_"*22 + f"\nName: {name}\nSurname: {surname}\nSex: {sex}\nDate of birth։ {date_birtf}\nPhone: {tel}\nEmail: {email}\nSocial link: {soc_link}\nDate of registration: {date_time}"
            
    #         try: 
    #             img = get_profil_pic(insta_nik)
    #             bot.send_photo(chat_id=channel_id, photo=img, caption=mess)
    #             shutil.rmtree(insta_nik)
    #         except:
    #             bot.send_message(channel_id,mess)
    
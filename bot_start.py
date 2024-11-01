import telebot
from telebot import types
import requests
import time
import configparser
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 24) # Частота кадров
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # Ширина кадров в видеопотоке.
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Высота кадров в видеопотоке.

settings = configparser.ConfigParser()
settings.read('./MAIN/config.ini')
bot_key = settings['setup']['bot_key']
admin1 = int(settings['setup']['admin1'])
admin2 = int(settings['setup']['admin2'])
admlist = [admin1, admin2]
bot1 = telebot.TeleBot (bot_key)

@bot1.message_handler(content_types=['text'])
def get_text_messages(message):
    #print(message)
    #bot1.send_message(message.from_user.id, 'ok')
    print(f'Пользователь ID {message.from_user.id} : {message.from_user.first_name}')
    print(f'написал: {message.text}')
    print('')
    if message.text == '/cam' and message.from_user.id in admlist:
        ret, img = cap.read()
        cv2.imwrite('test.jpg', img)
        cap.release()
        #photo = ('test.jpg', 'rb')
        with open('test.jpg', 'rb') as photo:
            bot1.send_photo(message.from_user.id, photo)
            bot1.send_message(message.from_user.id, 'Задействован доступ администратора!')




if __name__ == "__main__":
    bot1.polling(none_stop=True, interval=10)
    pass
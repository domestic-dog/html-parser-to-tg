#!/usr/bin/env python3
import threading, sys
import time
import telebot
import os
bot = telebot.TeleBot("714857420:AAEvUuGHl2LvwABea8QAQfy6_trR_ZUmPnc")


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Представьтесь, пожалуйста')
#@bot.message_handler(commands=['check'])
#def send_check(message):
#    if trf != True:
#        msg = bot.send_message(message.chat.id, a, reply_markup=keyboard1) 
#    else:
#        msg = bot.send_message(message.chat.id, 'Все живы',reply_markup=keyboard1)

#keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
#keyboard1.row('/check')


def getStatus():
    threading.Timer(180, getStatus).start()
    trf = os.stat('/home/worker/vendingautm/status.txt').st_size == 0
    f = open('/home/worker/vendingautm/status.txt','r')
    a = f.read()
    if trf != True:
        bot.send_message('716082919', a)    
getStatus()        

bot.polling(none_stop=True, interval=0)

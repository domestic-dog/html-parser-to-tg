#!/usr/bin/env python3
import threading, sys
import time
import telebot
import hashlib
import os
bot = telebot.TeleBot("714857420:AAEvUuGHl2LvwABea8QAQfy6_trR_ZUmPnc") #token








def getStatus():
    threading.Timer(10, getStatus).start()
    сhecksize = os.stat('/home/worker/vendingautm/status.txt').st_size == 0
    openstatus = open('/home/worker/vendingautm/status.txt','r')
    readstatus = openstatus.read()
    hashstat= hashlib.md5(open('/home/worker/vendingautm/status.txt','rb').read()).hexdigest()
    readtemp = open('/home/worker/vendingautm/bot/temp.txt','r')
    hashtemp = hashlib.md5(open('/home/worker/vendingautm/bot/temp.txt','rb').read()).hexdigest()
    if сhecksize != True  and  hashtemp != hashstat:
#MESSAGES
        bot.send_message('589711771', readstatus)
        bot.send_message('266818872', readstatus)
        opentem = open('/home/worker/vendingautm/bot/temp.txt','w').close
        opentemp = open('/home/worker/vendingautm/bot/temp.txt','w')
        writetemp = opentemp.write(readstatus)    
        #FUCK TERMINAL SECTION
        #subprocess.call("sed -i '/75/d' /home/worker/vendingautm/status.txt", shell=True)
getStatus()        

bot.polling(none_stop=True, interval=0)

#!/usr/bin/env python3
import threading, sys
import time
import telebot
import hashlib
import csv
import os
import subprocess
bot = telebot.TeleBot("714857420:AAEvUuGHl2LvwABea8QAQfy6_trR_ZUmPnc") #token
data = {}


def get_who():
    a = subprocess.check_output("who | awk '{print $1 $5}'", shell=True)
    bot.send_message('589711771', a)
    bot.send_message('266818872', a)

def get_status():
    os.system("/home/worker/vendingautm/send_zeroReport.py")
    catStatus =  open('/home/worker/vendingautm/zeroStatus.txt', 'r')
    catStatusx = catStatus.read()
    catStatus.close()
    return catStatusx

@bot.message_handler(commands=['report'])
def send_something(message):
    try:
        bot.send_message('589711771', get_status())
        bot.send_message('266818872', get_status())
    except (ConnectionAbortedError, ConnectionResetError, ConnectionRefusedError, ConnectionError):
        time.sleep(5)
        bot.send_message('589711771', get_status())
        bot.send_message('266818872', get_status())

@bot.message_handler(commands=['check'])
def sends_something(message):
    get_who()




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

bot.polling(none_stop=True, interval=0, timeout=20)

#! /usr/bin/env python3
import requests

import config

import os

from bs4 import BeautifulSoup

import re


data = {'login':'d.podsytnik', 'password':'81dc9bdb52d04dc20036dbd8313ed055'}

begin = requests.Session()
headers = {'Content-type':'application/json'}
req = begin.post(config.login_url, json = data, headers=headers)
print(req.text)
i = 0
f = open('/home/worker/vendingautm/finally', 'w')
f.write("")
f.close
while i!=config.pages:
    r = begin.get(config.get_list_url + str(i))
    soup = BeautifulSoup(str(r.text), 'html.parser')
    r = r.text
    table = soup.find('tbody')
    r = str(table)
    final = BeautifulSoup(str(r),'html.parser')
    for a in final("a"):
        a.decompose()
    for script in final(["script", "style"]):
        script.decompose()
    for td in final("td"):
        td.find_all('td')
    all_text = ''.join(final.findAll(text=True))
    r = str(all_text)
    file =  open('/home/worker/vendingautm/finally', 'a')
    file.write(r)    
    file.close()
    i+=1

os.system("sed -i '/^$/d' /home/worker/vendingautm/finally ")



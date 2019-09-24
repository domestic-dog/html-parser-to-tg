#!/usr/bin/env python3
import psycopg2

conn = psycopg2.connect(dbname='listdb', user='worker')
cursor = conn.cursor()













file_to_open = "/home/worker/vendingautm/parselist/termlist"
f = open(file_to_open)
class Terminal:
  def __init__(self, id,term_name,agent,adress,uptime,money,status):
    self.id = id
    self.term_name = term_name
    self.agent = agent
    self.adress = adress
    self.uptime = uptime
    self.money = money
    self.status = status

id = 0
term_name = 1
agent = 2
adress = 3
uptime = 4
money = 5
status = 6
file = open('./temp.txt', 'w')
result =f.read().splitlines()
#for i in range(112):
while result: 
   # print(result[id] + result[status])
    str = Terminal(result[id],result[term_name],result[agent],result[adress],result[uptime],result[money],result[status])
    id+= 7
    status+= 7
    term_name+=7
    agent+=7
    uptime+=7
    money+=7
    adress+=7
    file.write(str.id+ str.term_name+ str.agent + str.status + '\n')
    print(str.__dict__)

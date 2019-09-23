#!/usr/bin/env python3
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
result =f.read().splitlines()
#for i in range(112):
while result: 
   # print(result[id] + result[status])
    str= Terminal(result[id],result[term_name],result[agent],result[adress],result[uptime],result[money],result[status])
    id+= 7
    status+= 7
    print(str.id + str.status)

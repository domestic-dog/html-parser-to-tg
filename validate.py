#!/usr/bin/env python3
import subprocess
import csv

data = {}

with open('/home/worker/vendingautm/temp.csv','r') as fin:
    reader=csv.reader(fin, skipinitialspace=True, quotechar="'") 
    for row in reader:
        data[row[0]] =row[1]
#print(data)
d = open('/home/worker/vendingautm/temp.csv', 'w').close()
d
e = open('/home/worker/vendingautm/status.txt', 'w').close()
e

subprocess.call("/home/worker/vendingautm/parse.sh")

#_________get cvs


#openfile
file_to_open = "/home/worker/vendingautm/termlist"
f = open(file_to_open, 'r' )

id = 0
term_name = 1
agent = 2
adress = 3
uptime = 4
money = 5
status = 6
newdata = {}
file = open('/home/worker/vendingautm/temp.csv', 'w')
sfile = open('/home/worker/vendingautm/status.txt', 'w')
result =f.read().splitlines()
while  result :
    try:
        #print(result[id] + result[status])
        file.write(result[id].lstrip() +',' + result[status].lstrip()  + '\n' )
        newdata[result[id].lstrip()] =result[status].lstrip() 
        id+=7
        status+= 7
        term_name+=7
        agent+=7
        uptime+=7
        money+=7
        adress+=7
    except IndexError:
        break;
#print(newdata)

#End of get infoList
#------------------
for i in data:
    if data[i] != newdata[i]:
        sfile.write('Terminal: '+ i + ' ' + data[i] + ' -> ' + newdata[i] + '\n')


#!/usr/bin/env python3
import subprocess
import csv

data = {}

with open('temp.csv','r') as fin:
    reader=csv.reader(fin, skipinitialspace=True, quotechar="'") 
    for row in reader:
        data[row[0]] =row[1]
print(data)















subprocess.call("./parselist/parse.sh")

#_________get cvs


#openfile
file_to_open = "/home/worker/vendingautm/parselist/termlist"
f = open(file_to_open)

id = 0
term_name = 1
agent = 2
adress = 3
uptime = 4
money = 5
status = 6
newdata = {}
file = open('temp.csv', 'w')
result =f.read().splitlines()
while  result :
    try:
        #print(result[id] + result[status])
        file.write(result[id] +',' + result[status].lstrip()  + '\n' )
        newdata[result[id]] =result[status].lstrip() 
        id+=7
        status+= 7
        term_name+=7
        agent+=7
        uptime+=7
        money+=7
        adress+=7
        # file.write(result[id] +',' + result[status].lstrip()  + '\n' )
    except IndexError:
        break;


#End of get infoList




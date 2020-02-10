#!/usr/bin/env python3
import csv
data = {}
x = ''
f = open('/home/worker/vendingautm/zeroStatus.txt', 'w');
with open('/home/worker/vendingautm/temp.csv','r') as fin:
        reader=csv.reader(fin, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[int(row[0])] = str(row[1]), int(row[2].replace('\xa0',''))
def getzeroTerminals(data):
    f.write('Нулевые терминалы:' + '\n')
    for i in data:
        try:
            if str(data[i][0]) == 'Работает' and data[i][1] == 0:
                f.write('Terminal: ' + str(i) + '\n')
        except KeyError:
            continue
        
getzeroTerminals(data)














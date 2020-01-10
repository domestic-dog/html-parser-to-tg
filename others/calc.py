#!/usr/bin/env python3
import sys
import csv
import lunh
#ARGS

firstticket = sys.argv[1]
lastticet = sys.argv[2]

#/ARGS

#MAIN FUNCTION

def calcsql(first,last):
    lens = len((first))
    lens2 = len((last))
    if lens == 16 and lens2 == 16 and check_numbers(firstticket,lastticet) == True:
        print('Тип билета: Моментальный')
        print('Тип игры ' +  bet_type(first,7))
        print('Последняя пачка ' + last_pack(last))
        print('Первый Номер ' + number(first))
        print('Последний номер ' + number(last))
        print(generate("first"))
        
        bettype  = bet_type(first,7)
        lastpack = last_pack(last)
        firstnumber = number(first)
        lastnumber = number(last)
        



        #print('psql -d terminal -c \"\update bet_dispenser_status set bet_count=\'250\', first_bet_num=  \'5100718159150007\', current_bet_num= \'5100718159150700\',  current_pack_num=\'510071815915\', first_pack_num=  \'510071815915\',        bet_type=        \'30510\',         pack_count=\'2\',         pack_size='\160\',         draw_id=\'0\',        utilized=\'f\', design_id=\'AF\' where dispenser_id=\'9\';\"')
    else:
        print('Билет указан неправильно')
        exit()            
    

#HELPER FUNCTIONS

def bet_type(first,count):
    return first[:count]

def last_pack(last):
    return last[7:-4]


def number(number):
    return number[12:]

def check_numbers(first,last):
    if  first[:-6] == last[:-6]:
        return True


calcsql(firstticket,lastticet)


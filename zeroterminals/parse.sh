#!/bin/bash
rm -f /home/employer/termlist
curl -s -d  '{login:"n.potapov", password:"6ad9bdb8982f70b1097615e4f94e760d"}' -c /home/employer/cookie  -H "Content-Type:application/json" -X POST  https://v2.vendingloto.ru/api/login/index 
curl -s -b /home/employer/cookie -o /home/employer/file#1  https://v2.vendingloto.ru/terminal/terminallist?pagenumber=[0-4];echo ''
cat /home/employer/file* >> /home/employer/termlist;rm /home/employer/file*
for term in $(cat ~/active_terminals); do
where=$(grep -am1 -B11 "terminal/card/$term" /home/employer/termlist|sed -E 's/&#[[:digit:]]{3};|td|\/|&quot;//g'|tr -s ' '|sed -n '1p'|cut -d\> -f2|cut -d\< -f1);
who=$(grep -am1 -B11 "terminal/card/$term" /home/employer/termlist|sed -E 's/&#[[:digit:]]{3};|td|\///g'|tr -s ' '|sed -n '2p'|cut -d\> -f2|cut -d\< -f1);
money=$(grep -am1 -B11 "terminal/card/$term" /home/employer/termlist|sed -E 's/&#[[:digit:]]{3};|td|\///g'|tr -s ' '|sed -n '7p'|cut -d\> -f2|cut -d\< -f1|rev|cut -c2-|rev);
status=$(grep -am1 -B11 "terminal/card/$term" /home/employer/termlist|sed -E 's/&#[[:digit:]]{3};|td|\///g'|tr -s ' '|sed -n '9p'|cut -d\> -f2|cut -d\< -f1);
if [[ $money -eq 0 ]]; then echo "$term $where $who $status";fi
done
rm -f /home/employer/termlist
#grep -a "$(printf '\u20bd')" termlist|sed 's/&#160;//g'|tr -d ' '|cut -c5-|rev|cut -c8-|rev


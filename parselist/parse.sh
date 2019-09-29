#!/bin/sh
rm  termlist
curl -s -d  '{login:"d.podsytnik", password:"81dc9bdb52d04dc20036dbd8313ed055"}' -c cookie  -H "Content-Type:application/json" -X POST  https://v2.vendingloto.ru/api/login/index
curl -s -b cookie -o file#1  https://v2.vendingloto.ru/terminal/terminallist?pagenumber=[0-6];echo ''
cat file* |pup 'td'| sed '/td/d' | sed '/btn/d' | sed '/fa fa-info-circle/d'| sed '/fa fa-pencil/d'| sed '/d>/d'| sed '/a>/d'| sed '/i>/d'|  sed '/span/d' >> termlist;rm file*
#cat termlist

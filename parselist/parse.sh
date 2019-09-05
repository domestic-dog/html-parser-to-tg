#!/bin/bash
rm -f termlist
curl -s -d  '{login:"d.podsytnik", password:"81dc9bdb52d04dc20036dbd8313ed055"}' -c cookie  -H "Content-Type:application/json" -X POST  https://v2.vendingloto.ru/api/login/index
curl -s -b cookie -o file#1  https://v2.vendingloto.ru/terminal/terminallist?pagenumber=[0-4];echo ''
cat file* >> termlist;rm file*

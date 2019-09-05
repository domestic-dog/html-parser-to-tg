#!/bin/bash
curl -s -d  '{login:"d.podsytnik", password:"81dc9bdb52d04dc20036dbd8313ed055"}' -c cookie  -H "Content-Type:application/json" -X POST  https://v2.vendingloto.ru/api/login/index
curl -s -b cookie -o list1.html  https://v2.vendingloto.ru/terminal/terminallist
curl -s -b cookie -o list2.html  https://v2.vendingloto.ru/terminal/terminallist?pagenumber=1
curl -s -b cookie -o list3.html  https://v2.vendingloto.ru/terminal/terminallist?pagenumber=2
curl -s -b cookie -o list4.html  https://v2.vendingloto.ru/terminal/terminallist?pagenumber=3

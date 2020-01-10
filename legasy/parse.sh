#!/bin/sh
source $HOME/.bash_profile
rm -f  /home/worker/vendingautm/termlist
curl -s -d  '{login:"d.podsytnik", password:"81dc9bdb52d04dc20036dbd8313ed055"}' -c /home/worker/vendingautm/cookie  -H "Content-Type:application/json" -X POST  https://v2.vendingloto.ru/api/login/index > /dev/null
curl -s -b /home/worker/vendingautm/cookie -o /home/worker/vendingautm/file#1  https://v2.vendingloto.ru/terminal/terminallist?pagenumber=[0-6];echo ''
cat /home/worker/vendingautm/file* | pup 'td'| sed '/td/d' | sed '/btn/d' | sed '/fa fa-info-circle/d'| sed '/fa fa-pencil/d'| sed '/d>/d'| sed '/a>/d'| sed '/i>/d'|  sed '/span/d' >> /home/worker/vendingautm/termlist; rm -f /home/worker/vendingautm/file*
#cat termlist

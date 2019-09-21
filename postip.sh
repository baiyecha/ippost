curl http://www.net.cn/static/customercare/yourip.asp | grep --text -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" > ip
git add -A
git commit --amend --no-edit
git push origin master -f






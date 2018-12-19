import os
import json
import time
fp=open('cred.txt')
data=fp.read()
fp.close()
cred=json.loads(data)


os.chdir(cred["filepath"])
os.system('git init')
os.system('git status')
os.system('git add .')
os.system('git status')
os.system('git commit -m {}'.format(cred["text"]))
os.system('git config --global user.email {}'.format(cred["email"]))
os.system('git config --global user.name {}'.format(cred["username"]))
os.system('git remote add origin {}'.format(cred["link"]))
os.system('git push -u origin master')


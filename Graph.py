import os
from random import randint
for i in range(1, 2000):
    for J in range(0, randint(1, 10)):
        d = str(i) + 'days ago'
        with open('file.text', 'a') as file:
            file.write(d)
            os.system('git add .')
            os.system('git commit --date="' + d + '" -m "commit"')
os.system('git push -u origin main')

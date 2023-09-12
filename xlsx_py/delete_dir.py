from genericpath import isfile
import os
import shutil
import time


all_dir = []

for dir in os.listdir(): # find all folder and append list
    if '.' not in dir:
        all_dir.append(dir)

for dir in all_dir:
   shutil.rmtree(dir)

for dir in all_dir:
    os.mkdir(dir)

if os.path.isfile('M-CHAT-R.xlsx'):
    os.remove('M-CHAT-R.xlsx')
    print('Не забудьте внести в директорию актуальную таблицу!')
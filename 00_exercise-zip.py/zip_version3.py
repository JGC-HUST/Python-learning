#zip.py version3
#zip.py 可以用内置的zipfile 模块编写
import os
import subprocess
import time

source = r'C:\__Test__\1.txt'
target_dir = r'C:\__Test4__'

if not os.path.exists(target_dir):
      os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Enter a comment...')

if len(comment) > 0:
      target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
else:
      target = today + os.sep + now + '.zip'

if not os.path.exists(today):
      os.mkdir(today)
      print('Successfully created directory', today)

zip_command = 'zip -r {0} {1}'.format(target, source)

def run():
      print('Zip command is')
      print(zip_command)
      print('Running')
      if subprocess.call(zip_command) == 0:
            print('Successful backup to', target)
      else:
            print('Backup FAILED')

run()

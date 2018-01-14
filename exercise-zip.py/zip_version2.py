#zip.py version2
'''
      说明：先创建一级目录“C:\__Test__”之后才可以创建二级目录“today”
      否则会报错
'''
import os
import time
import subprocess
source = ['C:\\__Test__\\1.txt']
target_dir =  'C:\\__Test3__'

if not os.path.exists(target_dir):
      os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')
#print(target_dir)
#print(today)
#print(now)
target = today + os.sep + now + '.zip'
if not os.path.exists(today):
      os.mkdir(today)
      print('Successfully created directory', today)
zip_command = 'zip -r {0} {1}'.format(target, source[0])

print('Zip command is', zip_command)
print(zip_command)
print('Running:')
if subprocess.call(zip_command) == 0:
      print('Successful back up to', target)
else:
      print('Backup FAILED')

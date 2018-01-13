#zip.py
import os
import time
import subprocess
#源文件
source = ['C:\\__Test__\\1.txt']
#目标目录
target_dir = 'C:\\__Test2__'
#目标文件
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
#创建目标目录
if not os.path.exists(target_dir):
      os.mkdir (target_dir)
#压缩命令
zip_command = 'zip -r {0} {1}'.format (target, source[0])

print ('zip command is:')
print (zip_command)
print ('Running')
#执行压缩
if subprocess.call (zip_command) == 0:
      print('Successful backup to', target)
else:
      print('Backup FAILED')

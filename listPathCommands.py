import os
from os import path

pdirs = os.getenv('PATH')
pdirs_list = pdirs.split(':')
print(pdirs)

for dir in pdirs_list:
  #print(f"check commands from {dir}")
  if path.exists(dir):
    #print(f"dir {dir} exist")
    cmds = os.listdir(dir) 
    for cmd in cmds:
      if len(cmd) < 3:
        print(cmd)
  #print(cmds)

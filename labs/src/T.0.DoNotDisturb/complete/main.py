#!/usr/bin/env python

"""



"""
import asyncio
import os
import sys
import time
import subprocess

this_directory = os.path.dirname(__file__)
server_py = os.path.join(this_directory, 'server.py')
indicator_py = os.path.join(this_directory, 'indicator.py')

def main():
  print(f'running: {sys.executable} {server_py}')
  
  process_server = subprocess.Popen([sys.executable, server_py], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  process_indicator = subprocess.Popen([sys.executable, indicator_py], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

  for i in range(30):
    print(process_server.stdout.readlines(10))
    print(process_indicator.stdout.readlines(10))
    time.sleep(2)
  process_indicator.kill()
  process_server.kill()
  print('done')

if __name__ == '__main__':
  main()





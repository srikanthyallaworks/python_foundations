#!/usr/bin/env python

"""



"""

import os
import sys
import time
import subprocess


this_directory = os.path.dirname(__file__)


def run_script(script):
  return subprocess.Popen([sys.executable, script], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def run_indicator():
  indicator_py = os.path.join(this_directory, 'indicator.py')
  return run_script(indicator_py)


def run_server():
  server_py = os.path.join(this_directory, 'server.py')
  return run_script(server_py)


def main():
  with run_indicator() as process_indicator, run_server() as process_server:
    while True:
      print(process_server.stdout.readlines(10))
      print(process_indicator.stdout.readlines(10))
      time.sleep(2)
  print('Exiting')


if __name__ == '__main__':
  main()


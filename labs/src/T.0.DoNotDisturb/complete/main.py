#!/usr/bin/env python

"""



"""

import os
import sys
import time
import subprocess
from settings import get_settings
import webbrowser


this_directory = os.path.dirname(__file__)


def run_script(script):
  return subprocess.Popen([sys.executable, script], stdout=subprocess.PIPE)


def run_indicator():
  indicator_py = os.path.join(this_directory, 'indicator.py')
  return run_script(indicator_py)


def run_server():
  server_py = os.path.join(this_directory, 'server.py')
  return run_script(server_py)

def report_progress(process):
  for line in process.stdout:
    print(line)


def main():
  settings = get_settings()
  with run_indicator() as process_indicator, run_server() as process_server:
    webbrowser.open_new(f'http://127.0.0.1:{settings.port}')
    while True:
      report_progress(process_server)
      report_progress(process_indicator)
      time.sleep(5)



if __name__ == '__main__':
  main()


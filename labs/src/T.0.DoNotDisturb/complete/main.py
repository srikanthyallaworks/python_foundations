#!/usr/bin/env python
import os
import sys
import time
import subprocess
import webbrowser

try:
  from .settings import get_settings
except:
  from settings import get_settings


this_directory = os.path.dirname(__file__)


def run_script(script:str):
  """Runs the path as a python script

  Args:
      script ([str]): [description]

  Returns:
      [process]: handle for dealing with the process
  """
  return subprocess.Popen([sys.executable, script], stdout=subprocess.PIPE)


def run_indicator():
  """Runs ./indicator.py
  """
  indicator_py = os.path.join(this_directory, 'indicator.py')
  return run_script(indicator_py)


def run_server():
  """Runs the web server
  """
  server_py = os.path.join(this_directory, 'server.py')
  return run_script(server_py)

def report_progress(process):
  """Pipes output from the specified process to the terminal
  """
  for line in process.stdout:
    print(line)


def main():
  settings = get_settings()
  process_indicator= run_indicator()
  process_server=run_server() 
  webbrowser.open_new(f'http://127.0.0.1:{settings.port}')

  while True:
    report_progress(process_server)
    report_progress(process_indicator)
    time.sleep(1)


if __name__ == '__main__':
  main()


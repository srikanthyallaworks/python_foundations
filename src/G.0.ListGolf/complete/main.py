try:
  from .list_tools_tests import run_tests
except:
  from list_tools_tests import run_tests
import sys


def main():
  run_tests()  

if __name__ == '__main__':
  main()


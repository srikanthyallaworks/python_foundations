try:
  from .function_tools_tests import run_tests
except:
  from function_tools_tests import run_tests
import sys


def main():
  print(8**.5)
  return
  run_tests()  

if __name__ == '__main__':
  main()


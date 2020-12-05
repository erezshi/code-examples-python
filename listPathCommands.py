import os
from os import path
import re

local_path = os.getenv('PATH')
path_list = local_path.split(':')
regexp = re.compile('[^0-9a-zA-Z]+')


def solution1():
  for p in path_list:
    if path.exists(p):
      cmds = os.listdir(p) 
      for cmd in cmds:
        if len(cmd) == 2 and not regexp.match(cmd):
          print(cmd)


def solution2():
  files = []
  for p in path_list:
      if os.path.isdir(p):
        files_indir = [f for f in os.listdir(p) if path.exists(p) if not regexp.match(f)]
        files.extend(files_indir)

  result = list(filter(lambda x: len(x) == 2, files))
  print(result)

def fizzbuzz():
  for n in range(1, 100):
    # print(n)
    if n % 3 == 0 and n % 5 == 0:
      print("FizzBuzz")
    elif n % 3 == 0:
      print("Fizz")
    elif n % 5 == 0:
      print("Buzz")
    else:
      print(n)

def fib(number_of_items):
  counter = 0

  first = 0
  sencond = 1
  temp = 0
  while counter <= number_of_items:
    print(first)
    temp = first + sencond
    first = sencond
    sencond = temp
    counter += 1

def fib2(number):
  first = 0
  sencond = 1
  temp = 0
  for n in range(number, 0, -1):
    print(first)
    temp = first + sencond
    first = sencond
    sencond = temp





def main():
  # print("solution 1: \n")
  # solution1()
  # print("solution 2: \n")
  # solution2()
  # print("FizzBuzz")
  # fizzbuzz()
  # fib(10)
  fib2(10)

if __name__ == "__main__":
    main()
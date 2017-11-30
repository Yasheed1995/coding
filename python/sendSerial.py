from __future__ import print_function
import sys
import serial
import time
if len(sys.argv) != 3:
  print('Usage: python {} serialName'.format(sys.argv[0]))
  exit(-1)


def send():
# msg = "1000"
 s.write(sys.argv[2])
 time.sleep(1)
def read():
 try:
    while True:
      # line = s.readline()
      # print(line)
      # print(s.read(),end='')
      print(s.readline())
      sys.stdout.flush()
 except KeyboardInterrupt:
    print('\nExiting...')
    exit(-1)

if __name__ == '__main__': 
  s = serial.Serial(sys.argv[1], 9600)
  time.sleep(3)
  send()
  read()


import time
import random
import sys

while True:
  print 'hi {}'.format(time.time())
  if random.random() < .000001:
    print 'oh shit, something bad happened'
    sys.exit()

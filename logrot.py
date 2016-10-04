import os, shutil, sys
from datetime import datetime

out_path = os.path.expanduser(' '.join(sys.argv[1:]))

def write_rotate(line):
  with open(out_path, 'a') as f:
   f.write('{} {}\n'.format(datetime.utcnow(), line))

  # limit files to 10 MB
  if os.path.getsize(out_path) > 10 * 1024 ** 2:
    shutil.move(out_path, out_path + '.old')

def read_forever():
  write_rotate('---begin logrot piped output---')
  while True:
    try:
      write_rotate(raw_input())
    except EOFError:
      break
  write_rotate('---end logrot piped output---')

if __name__ == '__main__':
  read_forever()

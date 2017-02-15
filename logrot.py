import os, shutil, sys, traceback
from datetime import datetime


def write_rotate(out_path, line):
  with open(out_path, 'a') as f:
   f.write('{} {}\n'.format(datetime.utcnow(), line))

  # limit files to 10 MB
  if os.path.getsize(out_path) > 10 * 1024 ** 2:
    shutil.move(out_path, out_path + '.old')

def read_forever():
  out_path = os.path.expanduser(' '.join(sys.argv[1:]))

  def write_rotate_(line):
    write_rotate(out_path, line)

  write_rotate_('---begin logrot piped output---')
  try:
    while True:
      try:
        write_rotate_(raw_input())
      except EOFError:
        break
  finally:
    write_rotate_('---end logrot piped output---')

if __name__ == '__main__':
  try:
    read_forever()
  except:
    with open('logrot.err', 'a') as f:
      f.write('logrot exception\n')
      traceback.print_exc()

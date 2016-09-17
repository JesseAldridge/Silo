import os, shutil
from datetime import datetime


out_path = os.path.expanduser('~/logrot_out.txt')

def write_rotate(line):
  with open(out_path, 'a') as f:
   f.write('{} {}\n'.format(datetime.utcnow(), line))

  # limit files to 1 MB
  if os.path.getsize(out_path) > 1024 ** 2:
    shutil.move(out_path, out_path + '.old')

write_rotate('---begin logrot piped output---')
while True:
  try:
    write_rotate(raw_input())
  except EOFError:
    break
write_rotate('---end logrot piped output---')

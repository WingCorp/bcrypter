from bcrypt import hashpw, gensalt
from sys import stdin, argv

def encrypt(pw):
  pw = pw.encode('utf-8')
  salt = gensalt()
  hashed = hashpw(pw, salt)
  print(hashed)
  exit(0)

def read_from_stdin():
  for line in stdin:
    pw = line
    encrypt(pw)


if __name__ == "__main__":
  if len(argv) == 1:
    read_from_stdin()
  else:
    encrypt(' '.join(argv[1:]))
  pass
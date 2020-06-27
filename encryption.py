from keyGenerator import keys
from utils import convertCharToHex

plain_text = "Cryptography-128"

def init():
  arr = []
  for i in range(len(plain_text)):
    if (i % 4 == 0):
      column = []
      arr.append(column)
    column.append(convertCharToHex(plain_text[i]))
  return arr

print(init())





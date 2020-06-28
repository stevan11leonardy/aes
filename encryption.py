from keyGenerator import keys
from utils import (
  convertCharToHex, subbytesSbox, leftRotate,
  shiftRows, mixColumns, convertHexToChar
) 

plain_text = "Cryptography-128"

def init():
  arr = []
  for i in range(len(plain_text)):
    if (i % 4 == 0):
      column = []
      arr.append(column)
    column.append(convertCharToHex(plain_text[i]))
  return arr

cipher_text = init();

w = 0;
for i in range(11):
  if (i == 0):
    # add round key on round 0
    for j in range(len(keys[w])):
      for k in range(len(cipher_text[w])):
        cipher_text[w][k] = hex(
          int(cipher_text[w][k], 16) ^ int(keys[w][k], 16))
      w += 1
    
  elif (i == 10):
    # final round
    for j in range(4):
      cipher_text[j] = subbytesSbox(cipher_text[j].copy())
    
    cipher_text = shiftRows(cipher_text)

    for j in range(4):
      for k in range(4):
        cipher_text[j][k] = hex(
          int(cipher_text[j][k], 16) ^ int(keys[w][k], 16))
      w += 1


  else:
    # round 1 - 9
    for j in range(4):
      cipher_text[j] = subbytesSbox(cipher_text[j].copy())
    
    cipher_text = shiftRows(cipher_text)
    cipher_text = mixColumns(cipher_text)

    for j in range(4):
      for k in range(4):
        cipher_text[j][k] = hex(
          int(cipher_text[j][k], 16) ^ int(keys[w][k], 16))
      w += 1

r = []
for i in range(4):
  for j in range(4):
    r.append(convertHexToChar(cipher_text[i][j]))
  
print('cipher text: ' + ''.join(r))


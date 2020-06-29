from keyGenerator import keys
from utils import (
  convertCharToHex, invShiftRows,
  invSubbytesSbox, invMixColumns,
  convertHexToChar
)

keys_inv = []

w = len(keys)
for i in range(len(keys) // 4):
  for j in range(4, 0, -1):
    keys_inv.append(keys[w - j])
    
  w -= 4

cipher_text = ['\x0e', '¥', 'ù', '\x98', 'Á', '\t', '\x08', 'ø',
               '%', '×', '¸', '\x91', 'J', '<', 'K', 'Ü']

def init():
  arr = []
  for i in range(len(cipher_text)):
    if (i % 4 == 0):
      column = []
      arr.append(column)
    column.append(convertCharToHex(cipher_text[i]))
  return arr

plain_text = init()

w = 0;
for i in range(11):
  if (i == 0):
    # add round key on round 0
    for j in range(len(keys_inv[w])):
      for k in range(len(plain_text[w])):
        plain_text[w][k] = hex(
          int(plain_text[w][k], 16) ^ int(keys_inv[w][k], 16))
      w += 1
    
  elif (i == 10):
    # final round

    plain_text = invShiftRows(plain_text)

    for j in range(4):
      plain_text[j] = invSubbytesSbox(plain_text[j].copy())
    
    for j in range(4):
      for k in range(4):
        plain_text[j][k] = hex(
          int(plain_text[j][k], 16) ^ int(keys_inv[w][k], 16))
      w += 1


  else:
    # round 1 - 9
    plain_text = invShiftRows(plain_text)

    for j in range(4):
      plain_text[j] = invSubbytesSbox(plain_text[j].copy())
    
    for j in range(4):
      for k in range(4):
        plain_text[j][k] = hex(
          int(plain_text[j][k], 16) ^ int(keys_inv[w][k], 16))
      w += 1

    plain_text = invMixColumns(plain_text)


r = []
for i in range(4):
  for j in range(4):
    r.append(convertHexToChar(plain_text[i][j]))
  
print('plain text: ' + ''.join(r))
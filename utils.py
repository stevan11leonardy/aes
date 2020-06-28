
from table import (
  sbox, rcon, mixColumns as mc,
  sboxInv, mixColumnsInv as imc)

def convertCharToHex(char):
  return hex(ord(char))

def convertHexToChar(hex):
  return chr(int(hex, 16))

# arr -> array to be rotate; n -> how many times to rotate
def leftRotate(arr, n):
  temp = arr[:n]
  for i in range(len(arr) - n):
    arr[i] = arr[i + n]
  arr[len(arr) - n:] = temp
  return arr

def shiftRows(arr):
  d = [];
  for i in range(len(arr)):
    t = []
    for j in range(len(arr[i])):
      if (j == 0):
        t.append(arr[i][j])
      else:
        t.append(arr[(i + j) % 4][j])
    d.append(t)

  return d

def invShiftRows(arr):
  d = [];
  for i in range(len(arr)):
    t = []
    for j in range(len(arr[i])):
      if (j == 0):
        t.append(arr[i][j])
      else:
        t.append(arr[(i - j) % 4][j])
    d.append(t)

  return d

def mixColumns(arr):
  d = []
  n = []
  h = []

  p = 0
  for i in range(16):
    if (i % 4 == 0): 
      p = i
    w = p

    t = 0
    for j in range(4):
      t ^= galoisMult(int(arr[i % 4][j], 16), mc[w])
      w += 1
    d.append(hex(t))

  s = 0
  for i in range(4):
    t = []
    for j in range(4):
      t.append(d[s])
      s += 1
    n.append(t)

  for i in range(4):
    t = []
    for j in range(4):
      t.append(n[j][i])
    h.append(t)

  return h

def invMixColumns(arr):
  d = []
  n = []
  h = []

  p = 0
  for i in range(16):
    if (i % 4 == 0): 
      p = i
    w = p

    t = 0
    for j in range(4):
      t ^= galoisMult(int(arr[i % 4][j], 16), imc[w])
      w += 1
    d.append(hex(t))

  s = 0
  for i in range(4):
    t = []
    for j in range(4):
      t.append(d[s])
      s += 1
    n.append(t)

  for i in range(4):
    t = []
    for j in range(4):
      t.append(n[j][i])
    h.append(t)

  return h

def subbytesSbox(arr):
  for i in range(len(arr)):
    arr[i] = hex(sbox[int(arr[i], 16)])
  return arr

def invSubbytesSbox(arr):
  for i in range(len(arr)):
    arr[i] = hex(sboxInv[int(arr[i], 16)])
  return arr

def generateRCon(round):
  return [hex(rcon[round]), '0x00', '0x00', '0x00']

def xor(arr1, arr2):
  arr = []
  for i in range(len(arr1)):
    arr.append(hex(int(arr1[i], 16) ^ int(arr2[i], 16)))
  return arr

def galoisMult(a, b):
  p = 0
  hiBitSet = 0
  for i in range(8):
      if b & 1 == 1:
          p ^= a
      hiBitSet = a & 0x80
      a <<= 1
      if hiBitSet == 0x80:
          a ^= 0x1b
      b >>= 1
  return p % 256


# print(hex(galoisMult(0xf0, 2) ^ galoisMult(0x36, 3) ^ galoisMult(0xc5, 1) ^ galoisMult(0x63, 1)))
# print(hex(galoisMult(0xf0, 1) ^ galoisMult(0x36, 2) ^ galoisMult(0xc5, 3) ^ galoisMult(0x63, 1)))




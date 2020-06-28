from utils import convertCharToHex, leftRotate, subbytesSbox, xor, generateRCon

input_keys = "TugasKriptoSCC18"

# input_keys = input("Masukan kunci (16 karakter): ")

def initRoundKey():
  arr = []
  for i in range(len(input_keys)):
    if (i % 4 == 0):
      column = []
      arr.append(column)
    column.append(convertCharToHex(input_keys[i]))
  return arr

if (len(input_keys) > 16):
  print("Kunci max 16 karakter")
  keys = []
else:
  n = len(input_keys)
  if (n < 16):
    for i in range(16 - n):
      input_keys += '_'
      

  # start round 0
  keys = initRoundKey()

  # start round 1 - 10
  w = 3
  for i in range(10):
    for j in range(4):
      column = []
      if (j == 0):
        column = leftRotate(keys[w].copy(), 1)
        column = subbytesSbox(column)
        column = xor(column, generateRCon(i + 1))
        column = xor(column, keys[w - 3])
        keys.append(column)
      else:
        column = keys[w].copy()
        column = xor(column, keys[w - 3])
        keys.append(column)
      w += 1
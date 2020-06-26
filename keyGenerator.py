from table import sbox
from utils import convertCharToHex, leftRotate

input = "TugasKriptoSCC18"

def initRoundKey():
  arr = []
  for i in range(len(input)):
    if (i % 4 == 0):
      column = []
      arr.append(column)
    column.append(convertCharToHex(input[i]))
  return arr

# start round 0
keys = initRoundKey()

# start round 1 - 10

for i in range(10):
  column = []
  if (i == 0):
    column = leftRotate(keys[3], 1)
    keys.append(column)
  else:
    print(i)


print(sbox[43])


# print(bin(int(hexInput[0][0], 0))[2:].zfill(8))
# print(hexInput)


from table import sbox, rcon
def convertCharToHex(char):
  return hex(ord(char))

# arr -> array to be rotate; n -> how many times to rotate
def leftRotate(arr, n):
  temp = arr[:n]
  for i in range(len(arr) - n):
    arr[i] = arr[i + n]
  arr[len(arr) - n:] = temp
  return arr

def subbytesSbox(arr):
  for i in range(len(arr)):
    arr[i] = hex(sbox[int(arr[i], 16)])
  return arr

def generateRCon(round):
  return [hex(rcon[round]), '0x00', '0x00', '0x00']

def xor(arr1, arr2):
  arr = []
  for i in range(len(arr1)):
    arr.append(hex(int(arr1[i], 16) ^ int(arr2[i], 16)))
  return arr
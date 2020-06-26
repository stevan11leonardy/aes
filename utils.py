
def convertCharToHex(char):
  return hex(ord(char))

# arr -> array to be rotate; n -> how many times to rotate
def leftRotate(arr, n):
  temp = arr[:n]
  for i in range(len(arr) - n):
    arr[i] = arr[i + n]
  arr[len(arr) - n:] = temp
  return arr

def single_number(arr):
  num = 0
  for x in arr:
    num  ^= x
  return num

def main():
  print(single_number([1, 4, 2, 1, 3, 2, 3]))
  print(single_number([7, 9, 7]))

main()
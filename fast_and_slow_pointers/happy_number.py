def happy_number(num):
  fast, slow = num, num
  while True:
    slow = square_sum(slow)
    fast = square_sum(square_sum(fast))
    if slow == fast:
      break
  return slow == 1
    
def square_sum(num):
  _sum = 0
  while num > 0:
    digit = num %10
    _sum += digit*digit
    num //= 10
  return _sum

def main():
  print(happy_number(23))
  print(happy_number(12))

main()
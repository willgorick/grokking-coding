from turtle import right


def find_single_numbers(nums):
  n1xn2 = 0
  for num in nums:
    n1xn2 ^= num
  #n1nx2 is now the two missing numbers xor'd

  #get the rightmost bit that is 1 (different between the two)
  rightmost_set_bit = 1 
  # n1xn2 = 2 => 10
  
  #10 & 01 = 00
  #10 & 10 = 10
  while (rightmost_set_bit & n1xn2) == 0:
    rightmost_set_bit = rightmost_set_bit << 1 # 01 -> 10

  num1, num2 = 0, 0
  for num in nums: #xor one number by nums with the differntiating bit set, and the other by nums without it set
    if (num & rightmost_set_bit) != 0: #the bit is set
      num1 ^= num
    else:
      num2 ^= num
  
  return [num1, num2]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()
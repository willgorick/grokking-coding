#we know that a number xor it's complement will result in all 1's
# number ^ complement = all_bits_set
# number ^ number ^ complement = number ^ all_bits_set
# 0 ^ complement = number ^ all_bits_set
# complement = number ^ all_bits_set

def calculate_complement(num):
  bit_count, n = 0, num
  while n > 0: #count number of bits in num
    bit_count += 1
    n = n >> 1 #bitshift

  # if we take a number pow(2, n), then subtract 1 from it, we get a number with n bits of 1...i.e., 2^3 = 8, 8-1 = 7 which is 111 in binary (3 1's)
  all_bits_set = pow(2, bit_count) -1

  return num ^ all_bits_set

def main():
  print('Bitwise complement is: ' + str(calculate_complement(8))) #1000 -> 0111 (7)
  print('Bitwise complement is: ' + str(calculate_complement(10))) #1010 -> 0101 (5)

main()

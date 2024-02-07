"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to the number 1. All other (not-happy) numbers will never reach 1. Instead, they will be stuck in a cycle of numbers that does not include 1.

Given a positive number n, return true if it is a happy number otherwise return false.
Time Complexity: O(log(n)) using some funky math regarding the number of digits
Space Complexity: O(1)

"""

class Solution:
  def happy_number(self, num):
    
    slow, fast = num, num
    while True:
      slow = self.next_val(slow)
      fast = self.next_val(self.next_val(fast))
      if slow == fast:
        break
    return slow == 1
  
  def next_val(self, num):
    new_val = 0
    while num > 0:
      digit = num%10
      new_val += digit * digit
      num //= 10
    return new_val
  

def main():
  sol = Solution()
  print(sol.happy_number(23))
  print(sol.happy_number(12))
  

main()
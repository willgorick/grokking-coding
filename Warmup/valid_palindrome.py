"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
class Solution:
  def valid_palindrome(self, x):
    l, r = 0, len(x) -1
    while l <= r:
      while l < len(x)-1 and not x[l].isalpha():
        l += 1
      while r > 0 and not x[r].isalpha():
        r -= 1
      if x[l].lower() != x[r].lower():
        return False
      l += 1
      r -= 1
    return True
  
def main():
  sol = Solution()
  assert(sol.valid_palindrome("A man, a plan, a canal, Panama!") == True)
  assert(sol.valid_palindrome("nope") == False)
  assert(sol.valid_palindrome("Was it a car or a cat I saw?") == True)
  assert(sol.valid_palindrome("toot") == True)
  
  

if __name__ == "__main__":
  main()
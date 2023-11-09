"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""

class Solution:
  def sqrt(self, x):
    if x < 2:
      return x
    
    #binary search
    l, r = 2, x // 2
    pivot, squared = 0, 0
    while l <= r:
      pivot = l + ((r-l)//2)
      squared = pivot * pivot
      #pivot is sqrt
      if squared == x:
        return pivot
      #pivot was too large
      if squared > x:
        r = pivot - 1
      #pivot was too small
      else:
        l = pivot + 1
    #return right at the end because if squared was > x in last iteration of loop then r just decreased, if squared was less than x then now l > r
    return r



def main():
  sol = Solution()
  assert(sol.sqrt(25) == 5)
  assert(sol.sqrt(17) == 4)
  assert(sol.sqrt(8) == 2)

if __name__ == "__main__":
  main()
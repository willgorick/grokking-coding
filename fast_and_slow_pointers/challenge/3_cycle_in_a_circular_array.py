"""
We are given an array containing positive and negative numbers. Suppose the array contains a number 'M' at a particular index. Now, if 'M' is positive we will move forward 'M' indices and if 'M' is negative move backwards 'M' indices. You should assume that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

Time Complexity: O(n^2) - looping through each element and attempting to find a cycle for each so n^2
Space Complexity: O(1) just pointers

NOTE: We could improve our time complexity to O(n) by keeping track of each number we've looked at and whether or not it results in a cycle (this would allow us to skip that number in the outer for loop, or if we encounter it from any other starting number).  However, this would require us to include a set of space O(n).

"""
class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

class Solution:
  def __init__(self):
    self.array = []

  def detect_cycle(self, arr):
    self.array = arr
    
    #Look for a cycle starting from each element in the array
    for i in range(len(arr)):
      is_forward = arr[i] >= 0
      slow, fast = i, i

      while True:
        #slow moves forward 1, fast 2
        slow = self.move_through_array(slow, is_forward)
        fast = self.move_through_array(fast, is_forward)
        if fast != -1:
          #if the first step for fast didn't change directions, move again
          fast = self.move_through_array(fast, is_forward)

        #if both pointers are at the same index (excluding the -1 which indicates a direction change or one element cycle) then we have found a cycle
        if slow != -1 and slow == fast:
          return True
        #if either pointers found evidence of an invalid cycle (direction change or one element cycle) break
        if slow == -1 or fast == -1:
          break
    return False

  def move_through_array(self, index, is_forward):
    curr_num = self.array[index]
    curr_direction = curr_num >= 0

    #If the direction is different it is not a valid cycle, return -1
    if is_forward != curr_direction:
      return -1
    
    #Add current index to current number and then mod by len of array to make it circular
    next_index = (index + curr_num) % len(self.array)

    #One element cycles are NOT valid
    if next_index == index:
      return -1
    
    return next_index


def main():
  sol = Solution()
  print(sol.detect_cycle([1, 2, -1, 2, 2]))
  print(sol.detect_cycle([2, 2, -1, 2]))
  print(sol.detect_cycle([2, 1, -1, -2]))
  

main()
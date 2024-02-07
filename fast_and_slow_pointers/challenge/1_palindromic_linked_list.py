"""
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N) time complexity where 'N' is the number of nodes in the LinkedList.

Time Complexity: O(n) - reversing the list twice are each N/2, finding the midpoint is N/2, checking if reversed second half and first half are equal is N/2
Space Complexity: O(1) only storing pointers

"""

class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next


class Solution:
  def isPalindrome(self, head):
    slow, fast = head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    #slow is now the midpoint
    reversed_second_half = self.reverse(slow)
    #save a copy of the reversed second half that is still connected to head, we'll revert our reverse on this later to leave the linked list the way we received it
    copy_reversed_second_half = reversed_second_half

    while head and reversed_second_half:
      #if ever unequal, it's not palindromic
      if head.val != reversed_second_half.val:
        return False
      head = head.next
      reversed_second_half = reversed_second_half.next
      
    #reverse the list back so it's the same as when we got it
    self.reverse(copy_reversed_second_half)
    return True
  
  def reverse(self, head):
    prev = None
    while head:
      next = head.next
      head.next = prev
      prev = head
      head = next

    return prev


def main():
  sol = Solution()
  sol = Solution()
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(sol.isPalindrome(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(sol.isPalindrome(head)))
  

main()
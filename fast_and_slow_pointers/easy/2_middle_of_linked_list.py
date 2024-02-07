"""
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.

Time Complexity: O(n) because at most the slow pointer will get halfway through the total number of nodes
Space Complexity: O(1) just pointers

"""

class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

class Solution:
  def find_middle(self, head):
    fast, slow = head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow

def main():
  sol = Solution()
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Middle Node: " + str(sol.find_middle(head).val))

  head.next.next.next.next.next = Node(6)
  print("Middle Node: " + str(sol.find_middle(head).val))

  head.next.next.next.next.next.next = Node(7)
  print("Middle Node: " + str(sol.find_middle(head).val))

main()
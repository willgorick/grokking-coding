"""
Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Time Complexity: O(n) - finding midpoint is linear, reversing is linear, then rearranging is linear
Space Complexity: O(1) for pointers

"""
class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next


class Solution:
  def rearrange(self, head):
    if head is None or head.next is None:
      return head
    
    slow, fast, p1 = head, head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    #slow is now the midpoint
    p2 = self.reverse(slow)

    while p1 and p2:
      #save each pointer's next values
      next_p1 = p1.next
      next_p2 = p2.next
      #set our p1's next to the p2, and then that's next to our p1's original next 
      p1.next = p2
      p1.next.next = next_p1
      #set our new p1 to be the previous p1's next and our new p2 to the previous p2's next
      p1 = next_p1 
      p2 = next_p2

    #set the next of the last node to none to prevent loops
    if p1 is not None:
        p1.next = None
    return head
  
# 1 -> 2 -> 3
# 3 -> 2 -> 1 -> None
  def reverse(self, head):
    prev = None
    while head:
      next = head.next
      head.next = prev
      prev = head
      head = next
    return prev
    
  def print_list(self, head):
    temp = head
    while temp is not None:
      print(str(temp.val) + " ", end='')
      temp = temp.next
    print()

def main():
  sol = Solution()
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  sol.rearrange(head)
  sol.print_list(head)

  head2 = Node(2)
  head2.next = Node(4)
  head2.next.next = Node(6)
  head2.next.next.next = Node(8)
  head2.next.next.next.next = Node(10)
  sol.rearrange(head2)
  sol.print_list(head2)
  

main()
"""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

Time Complexity: O(n) several linear procedures are required (finding the cycle, finding the cycle length, offsetting by cycle length, and then looping through cycle until the two pointers meet). Each of these could take worst-case n steps if the entire linked list is a cycle
Space Complexity: O(1) for the pointers

"""
class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

class Solution:
  def start_of_cycle(self, head):
    cycle_length = 0
    slow, fast = head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast: #cycle found
        cycle_length = self.calculate_cycle_length(slow)
        break

    return self.find_start(head, cycle_length)

  def calculate_cycle_length(self, slow):
    curr = slow
    cycle_length = 0
    while True:
      curr = curr.next
      cycle_length += 1
      if curr == slow: #one full cycle completed
        break

    return cycle_length

  def find_start(self, head, cycle_length):
    p1, p2 = head, head
    for _ in range(cycle_length):
      p1 = p1.next

    while p1 != p2:
      p1 = p1.next
      p2 = p2.next

    return p1

def main():
  sol = Solution()
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(sol.start_of_cycle(head).val))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(sol.start_of_cycle(head).val))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(sol.start_of_cycle(head).val))
  

main()
from collections import deque
from re import A

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def is_palindrome_stack(head):
  queue = deque()
  slow, fast = head, head
  while fast.next is not None and fast.next.next is not None:
    queue.appendleft(slow.value)
    slow = slow.next
    fast = fast.next.next
  if fast.next is None:
    slow = slow.next #skip the middle number if odd
  while queue:
    queue_num = queue.popleft()
    if slow.value != queue_num:
      return False
    slow = slow.next
  return True
 

def is_palindrome_constant(head):
  slow, fast = head, head
  while fast.next is not None and fast.next.next is not None:
    slow = slow.next
    fast = fast.next.next
  reverse_first = reverse(slow)
  copy_reverse_first = reverse_first

  while head is not None and reverse_first is not None:
    if head.value != reverse_first.value:
      return False
    head = head.next
    reverse_first = reverse_first.next
  reverse(copy_reverse_first)

  if head is None or reverse_first is None:
    return True
  return False


def reverse(head):
  prev = None
  while (head is not None):
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome stack: " + str(is_palindrome_stack(head)))
  print("Is palindrome const: " + str(is_palindrome_constant(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome stack: " + str(is_palindrome_stack(head)))
  print("Is palindrome const: " + str(is_palindrome_constant(head)))

main()
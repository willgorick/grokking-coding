from collections import deque

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
  reverse_second = reverse(slow)
  copy_reverse_second = reverse_second

  while head is not None and reverse_second is not None:
    if head.value != reverse_second.value:
      return False
    head = head.next
    reverse_second = reverse_second.next
  reverse(copy_reverse_second)

  if head is None or reverse_second is None:
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
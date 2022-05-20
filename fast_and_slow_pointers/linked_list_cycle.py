from tracemalloc import start


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def linked_list_cycle(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
      length = calculateLength(slow)
      return True, length
  return False, None

def calculateLength(slow):
  curr = slow
  cycle_len = 0
  while True:
    curr = curr.next
    cycle_len += 1
    if curr == slow:
      break
  return cycle_len

def start_of_cycle(head):
  is_cycle, length = linked_list_cycle(head)
  if not is_cycle:
    return None
  first, second = head, head
  for x in range(length):
    second = second.next
  while first != second:
    first = first.next
    second = second.next
  return first

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  is_cycle, length = linked_list_cycle(head)
  if is_cycle:
    print("cycle found of length: " + str(length))
  else:
    print("cycle not found")
  start = start_of_cycle(head)
  if start:
    print("LinkedList cycle start: " + str(start.value))
  

  head.next.next.next.next.next.next = head.next.next

  is_cycle, length = linked_list_cycle(head)
  if is_cycle:
    print("cycle found of length: " + str(length))
  else:
    print("cycle not found")
  start = start_of_cycle(head)
  if start:
    print("LinkedList cycle start: " + str(start.value))


  head.next.next.next.next.next.next = head.next.next.next
  is_cycle, length = linked_list_cycle(head)
  if is_cycle:
    print("cycle found of length: " + str(length))
  else:
    print("cycle not found")
  start = start_of_cycle(head)
  if start:
    print("LinkedList cycle start: " + str(start.value))

main()
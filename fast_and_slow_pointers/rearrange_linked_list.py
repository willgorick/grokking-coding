class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def rearrange(head):
  if head is None or head.next is None:
    return

  slow, fast = head, head
  while fast.next is not None and fast.next.next is not None:
    slow = slow.next
    fast = fast.next.next
  flipped_end = reverse(slow)
  while head is not None and flipped_end is not None:
    temp = head.next #set first half's next to the second half, then advance first half head to it's original next
    head.next = flipped_end
    head = temp

    temp = flipped_end.next #set second half's next to first half, then advance second half head to it's original next
    flipped_end.next = head
    flipped_end = temp

def print_list(head):
  pretty_print = ""
  temp = head
  while temp is not None:
    pretty_print += str(temp.value) + " -> "
    temp = temp.next
  pretty_print += "None"
  print(pretty_print)

def reverse(head):
  prev = None
  while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  rearrange(head)
  print_list(head)

  new_head = Node(2)
  new_head.next = Node(4)
  new_head.next.next = Node(6)
  new_head.next.next.next = Node(8)
  new_head.next.next.next.next = Node(10)
  rearrange(new_head)
  print_list(new_head)


main()
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
  
  def print_list(self):
    temp = self
    while temp is not None:
      if (temp.next):
        print(temp.value, end=" -> ")
      else:
        print(temp.value)
      temp = temp.next

def reverse_every_k(head, k):
  if k <= 1 or head is None:
    return head

  prev, curr = None, head
  while True:
    last_node_prev = prev
    last_node_curr = curr
    i = 0
    while curr is not None and i < k: #handle chunk of size k
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
      i += 1
    
    if last_node_prev is not None:
      last_node_prev.next = prev
    else:
      head = prev

    last_node_curr.next = curr
    if curr is None:
      break
    prev = last_node_curr
  return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
from cgi import print_environ_usage
import re


class Node():
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
  def print_list(self):
    curr = self
    while curr is not None:
      if curr.next:
        print(curr.value, end=" -> ")
      else:
        print(curr.value)
      curr = curr.next

def reverse_sublist(head, p, q):
  if p == q:
    return head
  prev, curr = None, head
  i = 0
  while curr is not None and i < p -1:
    prev = curr
    curr = curr.next
    i += 1
  
  head_p = prev
  end_sub = curr

  while curr is not None and i < q:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    i += 1
  
  if head_p is not None:
    head_p.next = prev
  else: 
    head = prev
  end_sub.next = curr

  return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sublist(head, 2, 5)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
  def print_list(self):
    temp = self
    while temp is not None:
      if temp.next:
        print(temp.value, end=" -> ")
      else:
        print(temp.value)
      temp = temp.next

def rotate(head, rotations):
  if head is None or head.next is None or rotations <= 0:
    return head

  last_node = head
  list_len = 1
  while last_node.next is not None: #find list length and the last node
    last_node = last_node.next
    list_len += 1
  
  last_node.next = head #make the list circular
  rotations %= list_len #no need to do more rotations than the list length
  last_after_rotation = head
  skip_len = list_len - rotations

  for _ in range(skip_len - 1): #one fewer so we are at the new final value after rotation, rather than the new head
    last_after_rotation = last_after_rotation.next
  head = last_after_rotation.next #set new head
  last_after_rotation.next = None #de-cicularize the list
  return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()
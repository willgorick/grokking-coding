from heapq import *

class ListNode():
  def __init__(self, val):
    self.val = val
    self.next = None
  
  def __lt__(self, other):
    return self.val < other.val

def merge_lists(sorted_lists):
  min_heap = []
  for root in sorted_lists:
    heappush(min_heap, root) 
  
  result_head, result_tail = None, None
  while min_heap:
    node = heappop(min_heap)
    if result_head is None:
      result_head = result_tail = node #initialize head and tail to first node
    else: #add this node as prev's tail, make this the new prev
      result_tail.next = node
      result_tail = result_tail.next
    
    if node.next is not None: #if the node has a next, push it
      heappush(min_heap, node.next)

  return result_head

def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result is not None:
    print(str(result.val) + " ", end='')
    result = result.next
  print()

  l1 = ListNode(5)
  l1.next = ListNode(8)
  l1.next.next = ListNode(9)

  l2 = ListNode(1)
  l2.next = ListNode(7)

  result = merge_lists([l1, l2])
  print("Here are the elements form the merged list: ", end='')
  while result is not None:
    print(str(result.val) + " ", end='')
    result = result.next
  print()
  
main()

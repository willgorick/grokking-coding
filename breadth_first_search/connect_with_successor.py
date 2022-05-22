from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None
  def print_tree(self):
    curr = self
    while curr:
      print(str(curr.val), end="")
      if curr.next:
        print(" -> ", end="")
      curr = curr.next
    print()

def connect_with_successor(root):
  if root is None:
    return 
  queue = deque()
  queue.append(root)
  prev_node = root
  while queue:
    curr_node = queue.popleft()
    if prev_node:
      prev_node.next = curr_node
    prev_node = curr_node

    if curr_node.left:
      queue.append(curr_node.left)
  
    if curr_node.right:
      queue.append(curr_node.right)

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_with_successor(root)
  root.print_tree()

  new_root = TreeNode(1)
  new_root.left = TreeNode(2)
  new_root.right = TreeNode(3)
  new_root.left.left = TreeNode(4)
  new_root.left.right = TreeNode(5)
  new_root.right.left = TreeNode(6)
  new_root.right.right = TreeNode(7)
  connect_with_successor(new_root)
  new_root.print_tree()


main()
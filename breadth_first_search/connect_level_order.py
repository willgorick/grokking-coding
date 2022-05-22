from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val), end='')
        if current.next:
          print(" -> ", end="")
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()

def connect_level_order(root):
  if root is None:
    return
  
  queue = deque()
  queue.append(root)
  while queue:
    prev_node = None
    level_len = len(queue)
    for _ in range(level_len):
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
  connect_level_order(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()


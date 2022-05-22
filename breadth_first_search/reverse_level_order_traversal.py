from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def reverse_traverse(root):
  result = deque()
  if root is None:
    return result
  
  queue = deque()
  queue.append(root)
  while queue:
    level_size = len(queue)
    curr_level = []
    for _ in range(level_size):
      curr_node = queue.popleft()
      curr_level.append(curr_node.val)
      if curr_node.left:
        queue.append(curr_node.left)
      if curr_node.right:
        queue.append(curr_node.right)
    result.appendleft(curr_level)
  
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(reverse_traverse(root)))


main()

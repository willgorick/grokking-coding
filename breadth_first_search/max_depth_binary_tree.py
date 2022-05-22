from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def max_depth(root):
  max_depth = 0
  if root is None:
    return max_depth
  queue = deque()
  queue.append(root)
  while queue:
    len_level = len(queue)
    max_depth += 1
    for _ in range(len_level):
      curr_node = queue.popleft()
      if curr_node.left:
        queue.append(curr_node.left)
      if curr_node.right:
        queue.append(curr_node.right)
  return max_depth

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Maximum Depth: " + str(max_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Maximum Depth: " + str(max_depth(root)))


main()
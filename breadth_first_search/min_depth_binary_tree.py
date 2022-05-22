from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def min_depth(root):
  min_depth = 0
  if root is None:
    return 0
  queue = deque()
  queue.append(root)
  while queue:
    min_depth += 1
    level_len = len(queue)
    for _ in range(level_len):
      curr_node = queue.popleft()
      if not curr_node.left and not curr_node.right:   
        return min_depth
      if curr_node.left:
        queue.append(curr_node.left)
      if curr_node.right:
        queue.append(curr_node.right)
  return min_depth


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(min_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(min_depth(root)))
  root.left.left.right = TreeNode(2)
  root.left.left.right.right = TreeNode(14)
  root.right.right.left = TreeNode(7)
  print("Tree Minimum Depth: " + str(min_depth(root)))

main()
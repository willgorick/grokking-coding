from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def level_averages(root):
  result = []
  if root is None:
    return result
  queue = deque()
  queue.append(root)
  while queue:
    level_len = len(queue)
    level_sum = 0.0
    for _ in range(level_len):
      curr_node = queue.popleft()
      level_sum += curr_node.val
      if curr_node.left:
        queue.append(curr_node.left)
      if curr_node.right:
        queue.append(curr_node.right)
    level_avg = level_sum / level_len
    result.append(level_avg)

  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(level_averages(root)))

  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)
  print("Level averages are: " + str(level_averages(root)))

main()
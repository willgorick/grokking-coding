from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None
  
def zigzag(root):
  result = []
  if root is None:
    return result
  queue = deque()
  queue.append(root)
  reverse = True
  while queue:
    level_len = len(queue)
    curr_level = deque()
    for _ in range(level_len):
      curr_node = queue.popleft()
      if reverse: #if reversed, append the number to the left on the current level rather than the right
        curr_level.appendleft(curr_node.val)
      else:
        curr_level.append(curr_node.val)
      if curr_node.left:
        queue.append(curr_node.left)
      if curr_node.right:
        queue.append(curr_node.right)
    reverse = not reverse
    result.append(list(curr_level))

  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(zigzag(root)))


main()
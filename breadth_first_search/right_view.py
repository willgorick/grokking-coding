from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

def right_view(root):
  result = []
  if root is None:
    return result
  
  queue = deque()
  queue.append(root)
  while queue:
    level_len = len(queue)
    for i in range(level_len):
      curr_node = queue.popleft()
      if curr_node.left:
        queue.append(curr_node.left)
      if curr_node.right:
        queue.append(curr_node.right)
      if i == level_len-1: #append the last element of each level of the tree
        result.append(curr_node)

  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')
  print()

  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)
  result = right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')
  print()
main()

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def level_order_successor(root, key):
  if root is None:
    return None
  
  queue = deque()
  queue.append(root)
  while queue:
    curr_node = queue.popleft()
    if curr_node.left:
      queue.append(curr_node.left)
    if curr_node.right:
      queue.append(curr_node.right)
    
    if curr_node.val == key:
      break
  
  if queue:
    return queue.popleft()
  else: 
    return None
  
def main():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  
  result = level_order_successor(root, 3)
  if result:
    print(result.val)

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  
  result = level_order_successor(root, 9)
  if result:
    print(result.val)
  
  result = level_order_successor(root, 12)
  if result:
    print(result.val)


main()
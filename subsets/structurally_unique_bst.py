from turtle import left, right


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = left
    self.right = right

def find_unique_trees(n):
  if n <= 0:
    return []
  return find_trees_recursive(1, n)

def find_trees_recursive(start, end):
  result = []
  print(start,end)
  if start > end: #for 1 as the root, 1,0 (left) is None
    # for 2 as the root,  (right is none)
    result.append(None)
    return result

  for i in range(start, end+1): #1, 2: each number can be a root value
    left_subtrees = find_trees_recursive(start, i-1) #1,0
    right_subtrees = find_trees_recursive(i+1, end) #2,2
    for left_tree in left_subtrees:
      for right_tree in right_subtrees:
        root = TreeNode(i)
        print(i, left_tree, right_tree)
        root.left = left_tree
        root.right = right_tree
        result.append(root)
        print(result)
  return result

def main():
  trees_2 = find_unique_trees(2)
  trees_3 = find_unique_trees(3)
  print("Total trees: " + str(len(trees_2)))
  print("Total trees: " + str(len(trees_3)))
  for tree in trees_2:
    print(tree.val, tree.left, tree.right)
    left = tree.left
    right = tree.right
    if left:
      print("left: " + str(left.val))
    if right:
      print("right: " + str(right.val))


main()

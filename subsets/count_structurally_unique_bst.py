class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  
def count_trees_rec_setup(n):
  return count_trees({}, n)

def count_trees(map, n):
  if n in map: 
    return map[n]

  if n <= 1:
    return 1
  count = 0
  for i in range(1, n+1): #1 -> 1, 2 -> 1
    count_left_subtrees = count_trees(map, i-1) 
    count_right_subtrees = count_trees(map, n - i) 
    count += (count_left_subtrees * count_right_subtrees)
  map[n] = count
  return count
def main():
  print("Total trees: " + str(count_trees_rec_setup(2)))
  print("Total trees: " + str(count_trees_rec_setup(3)))
  print("Total trees: " + str(count_trees_rec_setup(4)))
  print("Total trees: " + str(count_trees_rec_setup(5)))


main()
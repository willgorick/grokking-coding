def find_subsets(nums):
  nums.sort()
  subsets = []
  subsets.append([])
  start_ind, end_ind = 0, 0
  for i in range(len(nums)): #for each number in the list
    start_ind = 0
    if i > 0 and nums[i] == nums[i-1]: #duplicate case
      start_ind = end_ind + 1 #how long the previous list was -1 (aka only add this number to the sets that already have it so we don't accidentally duplicate previously created sets)
      # explanation:
      # we have[[],[0],[1]] and we get a 1.  We only want to add the [1] to 0 and 1
    end_ind = len(subsets) -1
    for j in range(start_ind, end_ind+1):
      new_set = list(subsets[j])
      new_set.append(nums[i])
      subsets.append(new_set)
  return subsets
def main():
  print("Here is the list of subsets: " + str(find_subsets([0, 1, 1])))
  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3, 3])))


main()
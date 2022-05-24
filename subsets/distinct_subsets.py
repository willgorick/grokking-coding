
def subsets(nums):
  subsets = []
  subsets.append([])
  for num in nums:
    n = len(subsets)
    for i in range(n): #for each subset so far, new_subsets will include that subset and that subset + the current number
      new_subsets = list(subsets[i])
      new_subsets.append(num)
      print(new_subsets)
      subsets.append(new_subsets)
  return subsets
def main():
  print("Here is the list of subsets: " + str(subsets([1, 3])))
  print("Here is the list of subsets: " + str(subsets([1, 5, 3])))


main()

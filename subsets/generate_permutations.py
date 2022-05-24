from collections import deque

def permutations(nums):
  result = []
  permutations = deque()
  nums_len = len(nums)
  if nums_len == 0:
    return result
  permutations.append([]) #basically initialize with a value so we have something to start with
  for curr_num in nums:
    perm_len = len(permutations)
    for _ in range(perm_len): #for each perm we have, pull it out
      old_perm = permutations.popleft()
      for j in range(len(old_perm)+1):  #insert our new number at each point in the former permutation
        new_perm = list(old_perm)
        new_perm.insert(j, curr_num)
        if len(new_perm) == nums_len: #once we've reached the desired length, move them to results array
          result.append(new_perm)
        else:
          permutations.append(new_perm) #prior to desired length, store in queue
  return result

def generate_recusive_permutations(nums):
  result = []
  recursive_perms(nums, 0, [], result)
  return result
    
def recursive_perms(nums, index, curr_perm, result): # I donut understand
  if index == len(nums):
    result.append(curr_perm)
  else:
    for i in range(len(curr_perm) +1):
      new_perm = list(curr_perm)
      new_perm.insert(i, nums[index])
      recursive_perms(nums, index+1, new_perm, result)

def main():
  print(permutations([1,3,5]))
  print(generate_recusive_permutations([1,3,5]))

main()
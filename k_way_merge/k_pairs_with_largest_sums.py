from heapq import *

def k_pairs_with_largest_sum(nums1, nums2, k):
  min_heap = []
  for i in range(min(k, len(nums1))):
    for j in range(min(k, len(nums2))):
      if len(min_heap) < k:
        heappush(min_heap, (nums1[i] + nums2[j], i, j))
      else: #already pushed k sums to the heap
        if nums1[i] + nums2[j] < min_heap[0][0]: #no sums from here on will be larger
          break
        else:
          heappop(min_heap)
          heappush(min_heap, (nums1[i]+nums2[j], i, j))
  result = []
  while min_heap:
    num, i, j = heappop(min_heap)
    result.append([nums1[i], nums2[j]])
  return result


def main():
  print(k_pairs_with_largest_sum([9,8,2], [6,3,1], 3))
  print(k_pairs_with_largest_sum([5,2,1], [2,-1], 3))

main()
def target_sum(arr, target):
    pointer1 = 0
    pointer2 = len(arr)-1
    while pointer2 > pointer1:
        curr_sum = arr[pointer1] + arr[pointer2]
        if curr_sum == target:
            return [pointer1, pointer2]
        if curr_sum > target:
            pointer2 -= 1
        else:
            pointer1 += 1
    return [-1,-1]


def main():
    print(target_sum([1, 2, 3, 4, 6], 6))
    print(target_sum([2, 5, 9, 11], 11))


main()

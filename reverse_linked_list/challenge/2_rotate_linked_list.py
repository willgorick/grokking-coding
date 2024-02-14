"""
Given the head of a Singly LinkedList and a number 'k', rotate the LinkedList to the right by 'k' nodes.
RIGHT NOT LEFT


Time Complexity: O(n) because we mod by the list length we guarantee we will not do more than 2 cycles through the list
Space Complexity: O(1)
"""


class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def rotate_list(self, head, rotations):
        if rotations < 1 or not head:
            return head
        previous = None
        curr = head
        list_len = 1

        # find the length of the list by going until curr does not have a next val
        while curr.next:
            curr = curr.next
            list_len += 1

        # make the list circular then reset curr to head
        curr.next = head
        curr = head

        # mod the number of rotations by the list length so we don't waste time
        rotations %= list_len

        # the length we have to skip to get to the new head is the length of the list - the number of rotations
        skip_length = list_len - rotations

        # skip to the new head
        for _ in range(skip_length):
            previous = curr
            curr = curr.next

        # de-circularize the list so previous is the new tail
        previous.next = None
        return curr


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()


def main():
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    print_list(head)
    result = sol.rotate_list(head, 2)
    print("Nodes of rotated LinkedList are: ", end='')
    print_list(result)


main()

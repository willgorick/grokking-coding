"""
Given the head of a LinkedList and a number 'k', reverse every alternating 'k' sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than 'k' elements, reverse it too.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


def print_list(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.val, end=" -> ")
        else:
            print(curr.val)
        curr = curr.next


class Solution:
    def reverse_alernating_k_elements(self, head, k):
        if k <= 1 or not head:
            return head
        curr = head
        previous = None

        while curr:
            last_node_of_previous_part = previous
            last_node_of_current_part = curr
            i = k

            # reverse k nodes
            while curr and i > 0:
                next = curr.next
                curr.next = previous
                previous = curr
                curr = next
                i -= 1

            if last_node_of_previous_part:
                last_node_of_previous_part.next = previous
            # if last_node_of_previous_part was None that means this is the first sublist, so we set the head to previous (the first node in the now-reversed sublist)
            else:
                head = previous

            last_node_of_current_part.next = curr
            previous = last_node_of_current_part

            # leave k nodes as is
            i = k
            while curr and i > 0:
                previous = curr
                curr = curr.next
                i -= 1
        return head


def main():
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    print_list(head)
    result = sol.reverse_alernating_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    print_list(result)


main()

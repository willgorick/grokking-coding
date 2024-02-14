"""
Given the head of a LinkedList and two positions 'p' and 'q', reverse the LinkedList from position 'p' to 'q'.

Time Complexity: O(n) - each node is looked at one time (either skipping through it or reversing it)
Space Complexity: O(1) only pointers
"""


class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def reverse_sublist(self, head, p, q):
        if p == q:
            return head

        previous = None
        curr = head
        i = 1

        # skip nodes up to p
        while i < p and curr:
            previous = curr
            curr = curr.next
            i += 1

        # the list has three parts, the part before p, the reversed part from p to q, and the part after q
        # the last node of the first part has to be connected to the reversed start of the second part
        # the first node of the sublist becomes the last node after reversing and will be connected to the start of the third part
        last_node_of_first_part = previous
        last_node_of_sub_list = curr

        # reverse sublist
        while curr and i <= q:
            next = curr.next
            curr.next = previous
            previous = curr
            curr = next
            i += 1

        # if the last node of part 1 isn't null, set its next to the new start of the second part
        if last_node_of_first_part:
            last_node_of_first_part.next = previous
        # if the last node of part 1 is null, just set the head to the start of the second part (case where p is the first node)
        else:
            head = previous

        # the last node of the sublist (first node before reversal) is now connected to the start of part 3 of the list
        last_node_of_sub_list.next = curr

        return head


def print_list(head):
    temp = head
    while temp is not None:
        if temp.next:
            print(temp.val, end="->")
        else:
            print(temp.val)
        temp = temp.next


def main():
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    print_list(head)
    result = sol.reverse_sublist(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    print_list(result)
    result = sol.reverse_sublist(head, 1, 5)
    print("Nodes of reversed LinkedList are: ", end='')
    print_list(result)


main()

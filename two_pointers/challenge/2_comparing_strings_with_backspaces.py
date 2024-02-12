"""
Given two strings containing backspaces (identified by the character '#'), check if the two strings are equal.

Time Complexity: O(M + N) where M and N are the lengths of the two strings
Space Complexity: O(1) for the pointers

"""


class Solution:
    def compare_with_backspaces(self, str1, str2):
        p1, p2 = len(str1)-1, len(str2)-1

        while p1 >= 0 and p2 >= 0:
            # find the next characters to actually compare
            p1 = get_next_valid_char(str1, p1)
            p2 = get_next_valid_char(str2, p2)

            # if not equal, return false
            if str1[p1] != str2[p2]:
                return False
            # if both pointers are < 0, we've checked all characters without returning false, so they're equal
            if p1 < 0 and p2 < 0:
                return True
            # not both but only one of them less than zero
            if p1 < 0 or p2 < 0:
                return False
            # decrement both pointers to start the process of finding the next valid characters
            p1 -= 1
            p2 -= 1

        return True


def get_next_valid_char(str, pointer):
    backspace_count = 0
    while pointer >= 0:
        # add to our count of backspaces encountered
        if str[pointer] == "#":
            backspace_count += 1
            pointer -= 1
        # if not a backspace, but we have some backspaces stored up, use one and decrement the pointer
        elif backspace_count:
            pointer -= 1
            backspace_count -= 1
        # not a backspace and we don't have any stored up, so return this pointer
        else:
            return pointer
    return pointer


def main():
    sol = Solution()
    print(sol.compare_with_backspaces("xy#z", "xzz#"))
    print(sol.compare_with_backspaces("xy#z", "xyz#"))
    print(sol.compare_with_backspaces("xp#", "xyz##"))
    print(sol.compare_with_backspaces("xywrrmp", "xywrrmu#p"))


main()

"""
Given an absolute file path in a Unix-style file system, simplify it by converting ".." to the previous directory and removing any "." or multiple slashes. The resulting string should represent the shortest absolute path.

Time Complexity: O(n) consider each element 
Space Complexity: O(n) stack could contain all characters if the path given is already the shortest absolute path
"""


class Solution:
    def function_name(self, path):
        stack = []
        # split path on slashes
        split_path = path.split("/")
        for p in split_path:
            # if ".." pop from stack if possible
            if p == "..":
                if stack:
                    stack.pop()
            # if p is not "" or ".", append it
            elif p and p != ".":
                stack.append(p)
        # prepend a slash and join the parts on slash to make it an absolute path
        return "/" + "/".join(stack)


def main():
    sol = Solution()
    print(sol.function_name("/a/b/c"))
    print(sol.function_name("/a//b////c/d//././/"))
    print(sol.function_name("/a//b////c/d//././/.."))
    print(sol.function_name("/../"))
    print(sol.function_name("/home//foo/"))
    print(sol.function_name("/../../../../../.."))


main()

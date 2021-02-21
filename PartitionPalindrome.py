import traceback

class Solution:
    def partition(self, s):
        res = []
        self.dfs(s, [], res, 0)
        print(res)
        return res

    def dfs(self, s, path, res, depth):
        indent = ""
        for _ in range(0, depth):
            indent += " "
        called = indent + "dfs({}, {})".format(s, path)
        print(called)
        if not s:
            print(indent + "-" + "End of recursion")
            res.append(list(path))
            return
        print(indent + "-" + "for looping through this list {}".format(list(range(1, len(s) + 1))))
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                print(indent + "-" + "found palindrome: {}, i is currently {}".format(s[:i], i))
                path.append(s[:i])
                self.dfs(s[i:], path, res, depth + 1)
                rec = "dfs({}, {})".format(s[i:], path)
                removed = path.pop()
                print(indent + "-" + "Just finished recursive call to \"{}\" and {} was removed".format(rec, removed))
            else:
                print(indent + "-" + "{} is not a palindrome and i is {}".format(s[:i], i))

    def isPal(self, s):
        return s == s[::-1]

p = Solution()
p.partition('aab')


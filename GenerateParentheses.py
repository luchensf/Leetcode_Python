# def generateParenthesis( n):
#     res = []
#     s = [("(", 1, 0)]
#     while s:
#         print("before pop S", s)
#         x, l, r = s.pop()
#
#         print("after pop X:", x)
#         if l - r < 0 or l > n or r > n:
#             continue
#         if l == n and r == n:
#             print("current L and R", l, r)
#             res.append(x)
#
#         s.append((x+"(", l+1, r))
#         s.append((x+")", l, r+1))
#     return res


class Solution:

    def generateParentheses(self, n):
        self.n = n
        if self.n == 0:
            return []
        res = []
        self.generate(0, 0, '', res)
        return res

    def generate(self, l, r, x, res):
        if l == self.n and r == self.n:
            res.append(x)
        if l < self.n:
            self.generate(l + 1, r, x + '(', res)
        if r < self.n and r < l:
            self.generate(l, r + 1, x + ')', res)

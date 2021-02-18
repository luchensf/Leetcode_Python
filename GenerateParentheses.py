def generateParenthesis( n):
    res = []
    s = [("(", 1, 0)]
    while s:
        print("before pop S", s)
        x, l, r = s.pop()

        print("after pop X:", x)
        if l - r < 0 or l > n or r > n:
            continue
        if l == n and r == n:
            print("current L and R", l, r)
            res.append(x)

        s.append((x+"(", l+1, r))
        s.append((x+")", l, r+1))
    return res



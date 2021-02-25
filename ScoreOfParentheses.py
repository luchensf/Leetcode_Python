def scoreOfParentheses(S):
    res, l = 0, 0
    prev = None
    for a in S:
        # consider any open parentheses to the left of a pair of parentheses
        # is 2^l where l is number of open parentheses
        # (((()))) can be represented as 1 * 2 ^ 3
        # ((()())) can be represented as 1 * 2 ^2 + 1 * 2^2
        if a == "(":
            l += 1
        else:
            l -= 1
            if prev == "(":
                res += 2 ** l
        prev = a
    return res

scoreOfParentheses('(()(()()))')
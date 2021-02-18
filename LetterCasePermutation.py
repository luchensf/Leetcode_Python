def letterCasePermutation(S):
    output = [""]
    for c in S:
        tmp = []
        if c.isalpha():
            for o in output:
                tmp.append(o + c.lower())
                tmp.append(o + c.upper())
        else:
            for o in output:
                tmp.append(o + c)

        output = tmp
    return output


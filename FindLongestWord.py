def findLongestWord(s, d):
    best = ''
    for x in d:
        if (-len(x), x) < (-len(best), best):
            it = iter(s)
            if all(c in it for c in x):
                best = x
    return best


# s = "abpcplea"
# W = ["ale","apple","monkey","plea"]
# findLongestWord(s, W)
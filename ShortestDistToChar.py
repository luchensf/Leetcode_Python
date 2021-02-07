class Solution:
    """
        This solution is O(1.5n). For every element in the S, it'll assign d as the initial value until
        the first element of C was found.
        Then in the while loop, when i-j < ans[j] (initial assigned value), then it'll update the previous
        assigned value to i - j which should be the shortest distance until i - j is no longer smaller than ans[j].
    """
    def shortestToChar(self, s: str, c: str) -> List[int]:
        d = len(s)
        ans = [math.inf] * d
        for i in range(d):
            if s[i] != c:
                ans[i] = d
            else:
                ans[i] = 0
                j = i - 1
                while j >= 0 and (i - j) < ans[j]:
                    ans[j] = i - j
                    j -= 1
                d = 0
            d += 1
        return ans

def shortestToChar(s, c):
    """
        This solution is a O(2n) solution. It loops from the beginning and from the back at the same time.
        when s[i] == c, ans[i] will update to the current index, and lastcf will keep track the index of last C.
        when lastcf is not math.inf, then it'll try to find the min of assigned ans[i] and i - lastcf, which is
        the distance between i and index of last C.
        same to the loop of j. Basically by the end, it should find the min between i loop and j loop.
    """
    import math
    slen = len(s)
    ans = [math.inf] * slen
    lastcf = math.inf
    lastcb = math.inf

    for i, j in zip(range(slen), reversed(range(slen))):
        if s[i] == c:
            ans[i] = 0
            lastcf = i
        elif lastcf != math.inf:
            ans[i] = min(ans[i], i - lastcf)

        if s[j] == c:
            ans[j] = 0
            lastcb = j
        elif lastcb != math.inf:
            ans[j] = min(ans[j], lastcb - j)
    return ans

# shortestToChar('loveleetcode', 'e')



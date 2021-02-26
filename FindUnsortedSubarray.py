def findUnsortedSubarray(nums):
    s = sorted(nums)
    inds = []
    i = 0
    while i < len(s):
        if s[i] != nums[i]:
            inds.append(i)
        i += 1
    if not inds:
        return 0
    res = inds[-1] - inds[0] + 1
    return res


findUnsortedSubarray([2,6,4,8,10,9,15])




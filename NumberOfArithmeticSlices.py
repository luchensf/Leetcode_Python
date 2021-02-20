def numberOfArithmeticSlices(A):
    i = 1
    res = 0
    while i < len(A):
        diff = A[i] - A[i - 1]
        prev, nex = i, i + 1
        while nex < len(A) and A[nex] - A[prev] == diff:
            prev, nex = nex, nex + 1
        # nex is the first number that's out of the arithmetic sub-array
        # subtract i, which is the start of the sub-array, from nex then +1 to include the last number.
        dist = (nex - i + 1)
        if dist >= 3:
            res += int((dist - 1) * (dist - 2) / 2)
        i = nex
    return res

# solution from: https://tinyurl.com/pgf5f9hm
# class Solution:
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         count = comb = last_difference = 0
#         for i in range(len(A)-1):
#             difference= A[i+1] - A[i]
#             if i != 0 and difference == last_difference:
#                 comb += 1
#                 count += comb
#             else:
#                 comb = 0
#             last_difference = difference
#         return count
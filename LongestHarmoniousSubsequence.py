class Solution:
    def findLHS(self, nums) -> int:
        counter = {}
        lhs = 0
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
            if i - 1 in counter:
                lhs = max(lhs, counter[i-1] + counter[i])
            if i + 1 in counter:
                lhs = max(lhs, counter[i+1] + counter[i])
        return lhs

# s = Solution()
# s.findLHS([1,2, 3, 4])


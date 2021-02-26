class Solution:
    def sortArray(self, nums) :
        ## Merge Sort Solution
        def mergesort(nums):
            if len(nums) == 1:
                return nums
            m = len(nums) // 2
            left = mergesort(nums[:m])
            right = mergesort(nums[m:])
            return merge(left, right)

        def merge(arr_one, arr_two):
            d = []
            i, j = 0, 0
            while i < len(arr_one) and j<len(arr_two):
                if arr_one[i] <= arr_two[j]:
                    d.append(arr_one[i])
                    i += 1
                else:
                    d.append(arr_two[j])
                    j += 1
            d.extend(arr_two[j:] if i == len(arr_one) else arr_one[i:])
            return d
        return mergesort(nums)


s = Solution()
s.sortArray([5,1,1,2,0,0])


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge_sort(self, nums):
        if len(nums) == 1:
            return nums
        m = len(nums) // 2
        left = self.sortArray(nums[:m])
        right = self.sortArray(nums[m:])
        return self.merge(left, right)

    def merge(self, arr_one, arr_two):
        d = []
        while arr_one and arr_two:
            if arr_one[0] <= arr_two[0]:
                d.append(arr_one.pop(0))
            else:
                d.append(arr_two.pop(0))
        d.extend(arr_one if arr_one else arr_two)
        return d
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1

        while low < high:
            mid = low + (high - low) // 2

            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                # here to assign low, high to mid would avoid problem of missing the mountain index
                low = mid
            else:
                high = mid
        return mid


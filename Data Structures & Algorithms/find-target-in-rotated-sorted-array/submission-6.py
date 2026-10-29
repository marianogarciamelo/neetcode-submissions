class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def findMin():
            l, r = 0, n - 1
            while l < r:              # l < r is correct here, since r = m keeps m in range
                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return l

        def binarySearch(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1
            

        minIdx = findMin()
        if target > nums[-1]:
            return binarySearch(0, minIdx -1) # we dont want min
        else:
            return binarySearch(minIdx, n - 1)
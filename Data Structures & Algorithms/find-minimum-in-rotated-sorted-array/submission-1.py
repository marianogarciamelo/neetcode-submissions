class Solution:
    def findMin(self, nums: List[int]) -> int:
        # okay but you cant use math library return min(nums)
        l, r = 0, len(nums) - 1

        while l < r:
            m = (r+l) //2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
                
        return nums[l]
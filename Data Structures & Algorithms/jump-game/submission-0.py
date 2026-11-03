class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1 #index

        for i in range(n-1, -1, -1):
            maxJump = nums[i]
            if maxJump + i >= target:
                target = i
        return target == 0
        
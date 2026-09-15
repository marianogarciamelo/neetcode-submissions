class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sSet = set(nums)
        return (len(nums) != len(sSet))
     
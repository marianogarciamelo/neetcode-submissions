class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #indentation matters a lot in this context the specific return returns a list seen[difference] allows us to get the specicifc index we need for our list and then we also returnt the other index we are currently at looping
        seen = {}
        #make an enumurate remember index and fruits
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
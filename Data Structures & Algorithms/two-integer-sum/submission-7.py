class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            numberNeeded = target - nums[i]
            if numberNeeded in numMap:
                return [numMap[numberNeeded], i]
            numMap[nums[i]] = i



        
        
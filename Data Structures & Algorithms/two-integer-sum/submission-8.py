class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''numMap = {}

        for i in range(len(nums)):
            numberNeeded = target - nums[i]
            if numberNeeded in numMap:
                return [numMap[numberNeeded], i]
            numMap[nums[i]] = i
            '''

        numMap = {}

        for i, n in enumerate(nums):
            numberNeeded = target - n
            if numberNeeded in numMap:
                return [numMap[numberNeeded], i]
            numMap[n] = i




        
        
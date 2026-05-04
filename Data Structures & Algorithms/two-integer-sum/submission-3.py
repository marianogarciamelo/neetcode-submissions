class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val to index

        for i, n in enumerate(nums): # enumerate because we need value and index
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
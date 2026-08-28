class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}

        for i, n in enumerate(nums):
            number = target - n
            if number in seenMap:
                return [seenMap[number], i]
            seenMap[n] = i
        
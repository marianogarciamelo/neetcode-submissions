class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #O(1) lookup do not care about duplicates
        longest = 0 #my default if there is nothing then we have 0
        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
            
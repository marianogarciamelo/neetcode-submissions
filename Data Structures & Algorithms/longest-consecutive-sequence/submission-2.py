class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        longest = 0
        for num in res:
            if (num - 1) not in res:
                length = 0
                while (num + length) in res:
                    length += 1
                longest = max(length, longest)
        return longest 
        
        
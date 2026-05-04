class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


        """another way to do this you could make a key value pair and if > 1 then there is a duplicate
        counts = {}
            for num in nums:
                counts[num] = counts.get(num, 0) + 1
                if counts[num] > 1:
                    return True """
      
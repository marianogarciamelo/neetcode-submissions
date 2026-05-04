class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # i want to traverse the array adn check every index and as soon as i find one return True if not return False (this was brute force methoid)
        seen = set()
        for num in nums:
            if num in seen:
                return True            
            seen.add(num)
        return False   
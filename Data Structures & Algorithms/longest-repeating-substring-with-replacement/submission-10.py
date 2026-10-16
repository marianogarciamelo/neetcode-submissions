class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r = l = 0
        best = 0
        charCount = [0] * 26
        for r in range(len(s)):
            charCount[ord(s[r]) - ord('A')] += 1
            while ((r-l) + 1) - max(charCount) > k:
                charCount[ord(s[l]) - ord('A')] -= 1
                l += 1
            best = max(best, r-l+1)
        return best
            
            
        
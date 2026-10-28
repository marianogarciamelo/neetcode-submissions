class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = 0
        chars = [0] * 26
        for r in range(len(s)):
            chars[ord(s[r]) - ord('A')] += 1

            while (r - l + 1) - max(chars) > k:
                chars[ord(s[l]) - ord('A')] -= 1
                l += 1
            count = max(count, r-l+1)
        return count
        
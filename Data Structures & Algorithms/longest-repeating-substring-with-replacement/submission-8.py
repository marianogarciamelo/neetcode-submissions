class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        charList = [0] * 26

        for r in range(len(s)):
            charList[ord(s[r]) - ord('A')] += 1

            while (r-l+1) - max(charList) > k:
                charList[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, (r-l+1))
        return longest

            

        
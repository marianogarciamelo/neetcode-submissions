class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charS, charT = {}, {}

        for i in range(len(s)): #needed cause we are going through s and t if only one we could do c in s
            charS[s[i]] = charS.get(s[i], 0) + 1
            charT[t[i]] = charT.get(t[i], 0) + 1
        return charS == charT
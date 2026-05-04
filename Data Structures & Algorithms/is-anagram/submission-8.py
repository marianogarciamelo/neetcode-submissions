class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        anagramS, anagramT = {}, {}
        for i in range(len(s)): #range makes it 0 1 2 3 4 5 6
            anagramS[s[i]] = anagramS.get(s[i], 0) + 1
            anagramT[t[i]] = anagramT.get(t[i], 0) + 1
        return anagramS == anagramT
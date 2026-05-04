class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      
      anagramS, anagramT = {}, {}
      for i in range(len(s)):
        anagramS[s[i]] = anagramS.get(s[i], 0) + 1
        anagramT[t[i]] = anagramT.get(t[i], 0) + 1
      if anagramS == anagramT:
        return True
      return False

      
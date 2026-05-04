class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = defaultdict(list) #MAPPING CHARACTER COUNT TO LIST OF ANAGRAMS
      
      for words in strs:
         count = [0] * 26 #a....z #our words will look like 000002000100000000 for example
         for char in words:
           count[ord(char) - ord("a")] += 1 #char-"a" gives us the index to manipulate

         res[tuple(count)].append(words)
      return list(res.values())
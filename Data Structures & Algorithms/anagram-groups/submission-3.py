class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      #seperate each string in list
      #hashmap
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 #Initialize a count array of size 26 with all zeros
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
       
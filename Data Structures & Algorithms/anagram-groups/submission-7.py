class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            charCount = [0] * 26
            for c in str:
                charCount[ord(c) - ord('a')] += 1
            res[tuple(charCount)].append(str)
        return list(res.values())

        
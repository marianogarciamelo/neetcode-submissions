class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s #4s we use str before lengtt to make the 4 a char not an int
        return res
        
    def decode(self, s: str) -> List[str]:
        res, i = [], 0 #setting up a pointer and a new list
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length]) # + 1 to get outside of string
            i = j + 1 + length
        return res
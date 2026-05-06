class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        
    def decode(self, res: str) -> List[str]:
        newRes, i = [], 0 # pointer i to tell you where you at in the input string
        
        while i < len(res):
            j = i
            while res[j] != "#":
                j += 1
            length = int(res[i:j])
            newRes.append(res[j + 1 : j + 1 + length])
            i = j + 1 + length
        return newRes
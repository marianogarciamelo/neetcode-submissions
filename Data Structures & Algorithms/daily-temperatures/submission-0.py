class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ''' res = []
    res.append(0)
    stackOfTemps = []
    stackOfTemps.append(tempartures[-1])
    temparatures.pop()
    for i in reversed(temperatures):
        for j in reveresed(stackOfTemps):
            if [j] > [i]:
                res.append(len(stackOfTemps) - j)
    '''
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #0 is the first element since our list is a pair 
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res





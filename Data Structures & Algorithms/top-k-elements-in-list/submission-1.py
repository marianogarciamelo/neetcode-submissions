class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a hashmap
        '''hashNums = {}
        for num in nums:
            hashNums[num] = hashNums.get(num, 0) + 1
        return '''

        #BUCKETSORT count is key list of values
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n , 0)
        for n, c in count.items():
            freq[c].append(n) #this value n appears c times

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

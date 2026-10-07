class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #i want empty then 3
        res, curr = [], []
        n = len(nums)

        def dfs(i):
            if i == n:
                res.append(curr.copy())
                return
            #dont pick
            dfs(i+1)
            #pick
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
        
        dfs(0)
        return res
        
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #i can keep going and going and going and goung
        nums = sorted(nums)
        res = []

        def dfs(i , curr, runningtotal):
            if runningtotal == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(nums)):
                if runningtotal > target:
                    return
                curr.append(nums[j])
                dfs(j, curr, runningtotal + nums[j])
                curr.pop()
        
        dfs(0, [], 0)
        return res


            

        
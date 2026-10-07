class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def dfs(i, curr, sumtotal):
            if sumtotal == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(nums)):
                if sumtotal > target:
                    return
                curr.append(nums[j])
                dfs(j, curr, sumtotal + nums[j])
                curr.pop()
            
        dfs(0, [], 0)
        return res


        
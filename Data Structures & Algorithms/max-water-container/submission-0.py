class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) -1
        #with any two pointer approach l has to be less than r we never want the two to cross
        while l < r:
            area = min(heights[l], heights[r]) * (r - l) #area = length x width
            res = max(area, res)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res



        
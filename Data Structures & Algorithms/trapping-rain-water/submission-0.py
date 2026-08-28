class Solution:
    def trap(self, height: List[int]) -> int:
    
        if not height: return 0

        l, r = 0, len(height) -1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
    
    
    
    '''res = 0
    # start at index[1] 0 cannot hold any rain
    i = 1
    for i in range(1, len(heights)):
        if heights[i] == 0 and height[i-1] != 0 and heights[i+1] != 0:
            l, r = heights[i] - 1, heights[i] + 1
            area = min(height[l], height[r]) * (r - l - 1)
            while (l - 1 >= 0 and height[l-1] >= height[l]) or (r + 1 < len(height) and height[r+1] >= height[r]):          
                outerArea = min(height)
            #check the neighbors and then check the neighbors if the value keeps increasing

        area= min(height[l], height[r]) - height[i]




    max(area, res)
        


        #traverse the for loop and then find a 0 and then check the reach of that 0 '''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = {}
        res = []

        for n in nums2:
            while stack and stack[-1] < n:
                smaller = stack.pop()
                nextGreater[smaller] = n
            stack.append(n)
        
        for s in stack:
            nextGreater[s] = -1
        
        for n in nums1:
            res.append(nextGreater[n])
        
        return res
        

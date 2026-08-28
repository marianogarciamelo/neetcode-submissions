class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = {}

        for n in nums2:
            while stack and n > stack[-1]:
                smaller = stack.pop()
                nextGreater[smaller] = n

            stack.append(n)

        for n in stack:
            nextGreater[n] = -1

        return [nextGreater[n] for n in nums1]
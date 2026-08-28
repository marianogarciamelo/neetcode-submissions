# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and 
                    self.isSameTree(p.right,  q.right))
        
        return False
        
        '''
        bfsp = deque([p])
        bfsq = deque([q])

        while bfsp and bfsq:
            for i in range(len(bfsp)):
                nodep = bfsp.popleft()
                nodeq = bfsq.popleft()

                if nodep is None and nodeq is None:
                    continue
                if nodep is None or nodeq is None or nodep.val != nodeq.val:
                    return False
                bfsp.append(nodep.left)
                bfsp.append(nodep.right)
                bfsq.append(nodeq.left)
                bfsq.append(nodeq.right)
        
        return True
            
                
            
        
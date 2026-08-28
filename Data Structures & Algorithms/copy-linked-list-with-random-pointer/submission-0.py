"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None}

        currentPointer = head
        while currentPointer: #iterate once
            copy = Node(currentPointer.val)
            oldToCopy[currentPointer] = copy
            currentPointer = currentPointer.next
        
        currentPointer = head
        while currentPointer:
            copy = oldToCopy[currentPointer]
            copy.next = oldToCopy[currentPointer.next]
            copy.random = oldToCopy[currentPointer.random]
            currentPointer = currentPointer.next
        
        return oldToCopy[head]




        
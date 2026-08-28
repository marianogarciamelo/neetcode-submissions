# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    #can we do n-1 as like n-1.nexts or is that going to be bad in terms of memory #bad time complexity
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHalfList = slow.next
        prev = slow.next = None #end of our list
        
        while secondHalfList:
            temp = secondHalfList.next
            secondHalfList.next = prev
            prev = secondHalfList
            secondHalfList = temp

        # merge two halfs
        first, secondHalfList = head, prev
        while secondHalfList:
            temp1, temp2 = first.next, secondHalfList.next
            first.next = secondHalfList
            secondHalfList.next = temp1
            first = temp1
            secondHalfList = temp2
        

        

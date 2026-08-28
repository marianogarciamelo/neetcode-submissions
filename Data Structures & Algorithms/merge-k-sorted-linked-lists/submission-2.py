# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # list of linked lists use problem solving of merged linked lists 
        if not lists:
            return None
    
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i + 1 < len(lists):
                    list2 = lists[i+1]
                else:
                    list2 = None
                
                mergedLists.append(self.mergeTwoLists(list1, list2))
            lists = mergedLists

        return lists[0]
                
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
    
        while list1 and list2:
            if list2.val > list1.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2
        
        merged = dummy.next
        return merged


        
        
                

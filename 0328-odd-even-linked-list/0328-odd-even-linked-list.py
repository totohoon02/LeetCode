# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyOdd = ListNode(-1)
        dummyEven = ListNode(-1)
        
        count = 0
        
        curOdd = dummyOdd
        curEven = dummyEven
        curNode = head
        
        while curNode:
            if count % 2 != 0:
                curOdd.next = curNode
                curOdd = curOdd.next
            
            else:
                curEven.next = curNode
                curEven = curEven.next
            
            curNode = curNode.next
            curOdd.next = None
            curEven.next = None
            count+=1
            
        curEven.next = dummyOdd.next
        return dummyEven.next
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curNode = head
        
        while curNode:
            stack.append(curNode)
            curNode = curNode.next
        
        dummyNode = ListNode(-1)
        curNode = dummyNode
        
        while stack:
            curNode.next = stack.pop()
            curNode = curNode.next
        curNode.next = None
        
        return dummyNode.next
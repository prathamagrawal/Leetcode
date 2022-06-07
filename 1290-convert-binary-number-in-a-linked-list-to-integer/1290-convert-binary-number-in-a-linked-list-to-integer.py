# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num=0
        i=0
        t=head
        while(t):
            i+=1
            t=t.next
            
        for node in range(i):
            num+=head.val*pow(2,i-node-1)
            head=head.next
            
            
        return num
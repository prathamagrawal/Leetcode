# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length,t=0,head
        while(t):
            length+=1
            t=t.next
        if (length==1):
            return None
        
        temp=head
        
        for i in range((length//2)-1):
            temp=temp.next
        
        temp.next=temp.next.next
    
        return head
        
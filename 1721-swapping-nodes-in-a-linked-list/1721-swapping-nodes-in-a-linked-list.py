# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start,end=head,head
        
        length=0
        
        temp=start
        while(temp):
            length+=1
            temp=temp.next
        
        temp=k-1
        
        while(temp!=0):
            start=start.next
            temp-=1
        
        temp=length-k
        
        while(temp!=0):
            end=end.next;
            temp-=1
        
        temp=start.val
        start.val=end.val
        end.val=temp
        
        return head
        
            
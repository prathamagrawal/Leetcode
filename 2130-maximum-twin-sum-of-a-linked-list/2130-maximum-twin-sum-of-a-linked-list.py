# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l=[]
        while(head):
            l.append(head.val)
            head=head.next
        
        m=0
        
        for i in range(len(l)//2):
            temp=l[i]+l[len(l)-i-1]
            if(temp>m):
                m=temp
        
        return m
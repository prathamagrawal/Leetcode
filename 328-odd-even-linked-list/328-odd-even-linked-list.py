# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        length=0
        odd=[]
        even=[]
        while(t):
            if(length%2!=0):
                even.append(t.val)
                t=t.next
                
            else:
                odd.append(t.val)
                t=t.next
            length+=1
            
        m=head
        
        for i in odd:
            m.val=i
            m=m.next
        
        for i in even:
            m.val=i
            m=m.next
        
        return head
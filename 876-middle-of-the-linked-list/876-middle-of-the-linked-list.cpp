/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int length=0;
        ListNode* t=head;
        while(t!=NULL){
            length++;
            t=t->next;
        }
        int middle;
        if(length%2!=0){
            middle=length/2;
        }
        else{
            middle=(length/2);
        }
        
        
        for(int i=0;i<middle;i++){
            head=head->next;
        }
        return head;
    }
};
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
    int pairSum(ListNode* head) {
        int arr[100000];
        int m=0;
        
        while(head){
            arr[m]=head->val;
            head=head->next;
            m++;
        }
        
        int max=0,temp;
        for(int i=0;i<m/2;i++){
            temp=arr[i]+arr[m-i-1];
            if(temp>max){
                max=temp;
            }
        }
        return max;
        
    }
};
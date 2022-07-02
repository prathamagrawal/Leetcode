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
    vector<int> nextLargerNodes(ListNode* head) {
        vector <int> nums;
        while(head){
            nums.push_back(head->val);
            head=head->next;
        }
        
        int n=nums.size();
        
        vector <int> result (n);
        stack <int> temp;
        
        for (int i=n-1;i>=0;i--){
            while(!temp.empty() && nums[temp.top()] <=nums[i]){
                temp.pop();
            }
            if(!temp.empty()){
                result[i]=nums[temp.top()];
            }
            temp.push(i);
            
        }
        return result;
    }
};
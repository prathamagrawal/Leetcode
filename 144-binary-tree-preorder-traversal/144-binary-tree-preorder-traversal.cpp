/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    void preorder(TreeNode* root){
        if(!root){return;}
        result.push_back(root->val);
        if(root->left){
            preorder(root->left);
        }
        if(root->right){
            preorder(root->right);
        }
    }
    
    vector<int> preorderTraversal(TreeNode* root) {
        preorder(root);
        return result;
    }
private:
    vector<int> result;    
};
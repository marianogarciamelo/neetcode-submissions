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

    vector<int> mintomax;
    
    int kthSmallest(TreeNode* root, int k) {
        dfs(root);
        return mintomax[k-1];
    }

    void dfs(TreeNode* node) {
            if (!node) {
                return;
            }
            dfs(node->left);
            mintomax.push_back(node->val);
            dfs(node->right);
        }
};

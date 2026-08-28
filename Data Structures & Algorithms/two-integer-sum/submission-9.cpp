class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       int n = nums.size();
       unordered_map<int, int> numMap;

       for (int i = 0; i < n; i++) {
        int numberNeeded = target - nums[i];
        if (numMap.find(numberNeeded) != numMap.end()) {
            return {numMap[numberNeeded], i};
        }
        numMap.insert({nums[i], i});
       }
       return {};
    }
};

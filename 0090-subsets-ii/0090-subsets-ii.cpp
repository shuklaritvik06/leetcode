class Solution {
public:
    vector<vector<int>> helper(vector<int> &nums)
{
    vector<vector<int>> outer;
    outer.push_back(vector<int>{});
    int start = 0;
    int end = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        start = 0;
        if (i > 0 && nums[i] == nums[i - 1])
            start = end + 1;
        end = outer.size() - 1;
        int n = outer.size();
        for (int j = start; j < n; j++)
        {
            vector<int> internal(outer[j].begin(), outer[j].end());
            internal.push_back(nums[i]);
            outer.push_back(internal);
        }
    }
    return outer;
}
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
           sort(nums.begin(), nums.end());
    return helper(nums); 
    }
};
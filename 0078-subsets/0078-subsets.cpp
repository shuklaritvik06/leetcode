class Solution
{
public:
    void helper(int ind, vector<vector<int>> &ans, vector<int> ds, vector<int> &nums)
    {
        if (ind >= nums.size())
        {
            ans.push_back(ds);
            return;
        }
        ds.push_back(nums[ind]);
        helper(ind + 1, ans, ds, nums);
        ds.pop_back();
        helper(ind + 1, ans, ds, nums);

    }
    vector<vector<int>> subsets(vector<int> &nums)
    {
        vector<vector<int>> ans;
        vector<int> ds;
        helper(0, ans, ds, nums);
        return ans;
    }
};
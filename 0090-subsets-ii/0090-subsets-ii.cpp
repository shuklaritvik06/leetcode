class Solution
{
public:
    void helper(vector<int> &nums, int ind, vector<vector<int>> &result, vector<int> output)
    {
        if (ind >= nums.size())
        {
            result.push_back(output);
            return;
        }
        output.push_back(nums[ind]);
        helper(nums, ind + 1, result, output);
        output.pop_back();
        while (ind + 1 < nums.size() && nums[ind] == nums[ind + 1])
            ind += 1;
        helper(nums, ind + 1, result, output);
    }
    vector<vector<int>> subsetsWithDup(vector<int> &nums)
    {
        vector<vector<int>> result;
        vector<int> output;
        sort(nums.begin(), nums.end());
        helper(nums, 0, result, output);
        return result;
    }
};

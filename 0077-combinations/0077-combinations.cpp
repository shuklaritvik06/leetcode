class Solution
{
public:
    static vector<int> getArray(int n)
    {
        vector<int> temp;
        for (int i = 1; i <= n; i++)
            temp.push_back(i);
        return temp;
    }
    static void solve(vector<int> &nums, int index, vector<int> &output, vector<vector<int>> &result, int k)
    {
        if (index >= nums.size())
        {
            if (output.size() == k)
                result.push_back(output);
            return;
        }
        solve(nums, index + 1, output, result, k);
        output.push_back(nums[index]);
        solve(nums, index + 1, output, result, k);
        output.pop_back();
    }
    vector<vector<int>> combine(int n, int k)
    {
        vector<int> nums = getArray(n);
        vector<vector<int>> result;
        vector<int> output;
        solve(nums, 0, output, result, k);
        return result;
    }
};
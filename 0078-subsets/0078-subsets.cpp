class Solution
{
public:
    vector<vector<int>> subsets(vector<int> &nums)
    {
        vector<vector<int>> res;
        res.push_back(vector<int>{});
        for (auto num : nums)
        {
            int n = res.size();
            for (int i = 0; i < n; i++)
            {
                vector<int> internal(res[i].begin(), res[i].end());
                internal.push_back(num);
                res.push_back(internal);
            }
        }
        return res;
    }
};
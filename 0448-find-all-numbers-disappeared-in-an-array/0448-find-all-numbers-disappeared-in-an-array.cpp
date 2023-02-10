class Solution
{
public:
    vector<int> findDisappearedNumbers(vector<int> &nums)
    {
    vector<int> temp;
    int i = 0;
    while (i < nums.size())
    {
        int correctpos = nums[i] - 1;
        if (nums[i] <= nums.size() && nums[i] != nums[correctpos])
            swap(nums[i], nums[correctpos]);
        else
            i++;
    }
    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i] != i + 1)
            temp.push_back(i + 1);
    }
    return temp;
    }
};
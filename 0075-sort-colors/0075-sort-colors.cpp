class Solution
{
public:
    static int partition(vector<int> &arr, int start, int end)
    {
        int i = start - 1;
        int pivot = arr[end];
        for (int j = start; j <= end; j++)
        {
            if (arr[j] < pivot)
            {
                i++;
                swap(arr[j], arr[i]);
            }
        }
        swap(arr[i + 1], arr[end]);
        return i + 1;
    }
    void helperFunc(vector<int> &nums, int low, int high)
    {
        if (low < high)
        {
            int pi = partition(nums, low, high);
            cout << nums[pi] << endl;
            helperFunc(nums, low, pi - 1);
            helperFunc(nums, pi + 1, high);
        }
    }
    void sortColors(vector<int> &nums)
    {
        helperFunc(nums, 0, nums.size() - 1);
    }
};
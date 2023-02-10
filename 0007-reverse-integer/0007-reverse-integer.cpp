class Solution
{
public:
    int reverse(long long x)
    {
        long reverse = 0;
        bool isNegative = x < 0;
        x = abs(x);
        while (x > 0)
        {
            int digit = x % 10;
            reverse = digit + reverse * 10;
            x = x / 10;
        }
        if (reverse > INT_MAX || reverse < INT_MIN)
            return 0;
        if (isNegative)
            return -1 * reverse;
        else
            return reverse;
    }
};
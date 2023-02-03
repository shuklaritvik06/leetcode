class Solution {
public:
  int nthMagicalNumber(int n, int a, int b)
    {
        long  mod = pow(10, 9) + 7;
        long  mid;
        long  left = min(a,b);
        long  right = (long)n * min(a, b);
        while (left < right)
        {
            mid = left + (right - left) / 2;
            if ((mid / a) + (mid / b) - (mid / lcm(a, b)) < n)
                left = mid + 1;
            else
                right = mid;
        }
        return left % mod;
    }
};
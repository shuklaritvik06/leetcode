class Solution
{
public:
    int countPrimes(int n)
    {
        vector<bool> primes(n + 1, false);
        if (n <= 2)
            return 0;
        for (int i = 2; i * i <= n; i++)
        {
            if (!primes[i])
            {
                for (int j = 2 * i; j <= n; j += i)
                {
                    primes[j] = true;
                }
            }
        }
        int count = 0;
        for (int i = 2; i < n; i++)
        {
            if (!primes[i])
            {
                count++;
            }
        }
        return count;
    }
};
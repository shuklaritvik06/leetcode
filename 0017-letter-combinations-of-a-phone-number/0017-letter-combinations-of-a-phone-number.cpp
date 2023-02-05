class Solution
{
private:
    void doWork(string digits, string output, int index, vector<string> &result, unordered_map<char, string> mp)
    {
        if (index >= digits.size())
        {
            result.push_back(output);
            return;
        }
        string a = mp[digits[index]];
        for (int i = 0; i < a.size(); i++)
        {
            output.push_back(a[i]);
            doWork(digits, output, index + 1, result, mp);
            output.pop_back();
        }
    }

public:
    static unordered_map<char, string> letter_map()
    {
        unordered_map<char, string> mp;
        mp['2'] = "abc";
        mp['3'] = "def";
        mp['4'] = "ghi";
        mp['5'] = "jkl";
        mp['6'] = "mno";
        mp['7'] = "pqrs";
        mp['8'] = "tuv";
        mp['9'] = "wxyz";
        return mp;
    }
    vector<string> letterCombinations(string digits)
    {
        unordered_map<char, string> mp = letter_map();
        vector<string> result;
        if (digits.size() == 0)
            return result;
        string output = "";
        int index = 0;
        doWork(digits, output, index, result, mp);
        return result;
    }
};
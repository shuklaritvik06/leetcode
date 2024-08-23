class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal_num = 0
        temp = abs(x)
        while temp != 0:
            rem = temp % 10
            pal_num = pal_num * 10 + rem
            temp = temp // 10
        return pal_num == x
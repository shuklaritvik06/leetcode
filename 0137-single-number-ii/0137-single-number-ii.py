class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occurences = {}
        for i in nums:
            key = str(i)
            if occurences.get(key) is None:
                occurences[key] = 1
            else:
                occurences[key] += 1
        for key, val in occurences.items():
            if val == 1:
                return int(key)
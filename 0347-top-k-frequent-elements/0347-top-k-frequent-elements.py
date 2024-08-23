class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        if len(nums)==1 and k==1:
            return nums
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        result = [sorted_frequency[i][0] for i in range(0,k)]
        return result
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue            
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(target - total) < abs(target - closest_sum):
                    closest_sum = total                
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return total
        
        return closest_sum
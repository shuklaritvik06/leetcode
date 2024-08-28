class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_map = {}        
        for item in arr:
            count_map[item] = count_map.get(item, 0) + 1
        count_map = sorted(count_map.items(), key=lambda x: x[1])
        for ind, element in enumerate(count_map):
            if ind == k - 1 and element[1] == 1:
                return element[0]
        return ""
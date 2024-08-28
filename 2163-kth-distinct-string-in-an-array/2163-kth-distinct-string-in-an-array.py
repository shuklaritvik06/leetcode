class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_map = {}        
        for item in arr:
            count_map[item] = count_map.get(item, 0) + 1        
        filtered = filter(lambda x: x[1] == 1, count_map.items())        
        for ind, element in enumerate(list(filtered)):
            if ind == k - 1:
                return element[0]
        return ""
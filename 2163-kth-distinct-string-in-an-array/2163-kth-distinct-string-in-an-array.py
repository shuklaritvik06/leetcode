class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_map = {}        
        for item in arr:
            count_map[item] = count_map.get(item, 0) + 1
        count_map = count_map.items()
        distinct_count = 0
        for element in count_map:
            if element[1] == 1:
                distinct_count = distinct_count + 1
            if distinct_count == k and element[1] == 1:
                return element[0]
        return ""
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr_dict = {}
        target_dict = {}
        for item in arr:
            arr_dict[item] = arr_dict.get(item, 0) + 1
        for item in target:
            target_dict[item] = target_dict.get(item, 0) + 1
        for key, val in arr_dict.items():
            if key not in target_dict or target_dict[key]!=val:
                return False
        return True
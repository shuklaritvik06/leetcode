class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        result = ""
        for i in s:
            counter[i] = counter.get(i,0)+1
        sorted_dict = sorted(counter.items(), key=lambda x:x[1], reverse=True)
        for i in sorted_dict:
            result += i[0]*i[1]
        return result
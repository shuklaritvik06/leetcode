class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if anagrams.get(sorted_word) == None:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)        
        return list(anagrams.values())


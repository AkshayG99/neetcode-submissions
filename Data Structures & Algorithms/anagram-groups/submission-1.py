class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # key=tuple(list) value = []

        for word in strs:
            countWord = [0] * 26
            for char in word:
                countWord[ord(char) - 97] += 1
            
            groups[tuple(countWord)].append(word)
        
        return list(groups.values())



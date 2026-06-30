class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #from collections import defaultdict
        groups = defaultdict(list)
        # key: [0] * 26
        # value: [str]
        
        for word in strs:
            wordRep = [0] * 26
            for char in word:
                wordRep[ord(char) - 97] += 1
            groups[tuple(wordRep)].append(word)
        return list(groups.values())
                
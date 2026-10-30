class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res
    
    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        length = ""

        while i < len(s):
            while s[i].isnumeric():
                length += s[i]
                i += 1 
            strs.append(s[i+1:i + 1 + int(length)])
            i += 1 + int(length)
            length = ""
        return strs

            
            
        
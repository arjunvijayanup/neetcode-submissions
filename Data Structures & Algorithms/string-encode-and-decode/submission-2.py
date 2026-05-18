class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res
        

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j]) # Getting the length of string as an integer
            res.append(s[j + 1 : j + 1 + length]) # Extracting the string and appending to res list
            i = j + 1 + length # update i to new string delimiter start pos
        
        return res

        

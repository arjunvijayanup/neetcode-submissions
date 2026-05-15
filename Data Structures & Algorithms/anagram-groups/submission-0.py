class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            sorted_strs = ''.join(sorted(s))
            if sorted_strs not in hmap:
                hmap[sorted_strs] = []
            hmap[sorted_strs].append(s)
        
        return list(hmap.values())
                


        
            

        return sorted_strs

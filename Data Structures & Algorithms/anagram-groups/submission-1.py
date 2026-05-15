class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Default dict list creates empty list for a new key instead of raising KeyError
        hmap = defaultdict(list)
        for s in strs:
            sorted_strs = ''.join(sorted(s))
            hmap[sorted_strs].append(s)
        
        return list(hmap.values())
                


        
            

        return sorted_strs

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list) # mapping charecter count to list of Anagrams

        for s in strs:
            count = [0] * 26 # A-Z 26 Char
            for c in s:
                count[ord(c) - ord('a')] += 1 # Update count based on chars
            hmap[tuple(count)].append(s) # Keeping the char count as keys, appending strings having same char count keys

        return list(hmap.values()) # Returning values (string list) encapsulated in a list (List[List[str]])
                


        
            

        return sorted_strs

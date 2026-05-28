class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count, chmap = {}, {}
        l = 0
        for c in s1:
            chmap[c] = 1 + chmap.get(c, 0)
    
        for r in range(len(s2)):
            count[s2[r]] = 1 + count.get(s2[r], 0)
            if (r - l + 1) > len(s1):
                count[s2[l]] -= 1
                if count[s2[l]] == 0: # Removing key if the count is 0 so the dict == comparison returns true
                    del count[s2[l]]
                l += 1
            if count == chmap:
                return True
        
        return False
            




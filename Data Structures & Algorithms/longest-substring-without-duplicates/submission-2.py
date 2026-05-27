class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in char_set: # If right pointer char in our set (duplicate) - > Do this until char is out of set
                char_set.remove(s[left]) # Remove character in left pointer
                left += 1 # update pointer
            char_set.add(s[right])
            res = max(res, right - left + 1)
        
        return res









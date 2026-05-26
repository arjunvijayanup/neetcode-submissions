class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_s = set()
        res, left = 0, 0

        for right in range(len(s)):
            while s[right] in set_s:
                set_s.remove(s[left])
                left += 1
            set_s.add(s[right])
            res = max(res, right - left + 1)

        return res






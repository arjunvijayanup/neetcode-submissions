class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num # Intial streak and curr setup
            while curr in store: # Runs until curr is not in set
                streak += 1
                curr += 1
            res = max(res, streak)
        
        return res

            

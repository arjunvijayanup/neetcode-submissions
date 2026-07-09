class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, total):
            # Basecases
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i, subset, total + nums[i]) # Try all possible combinations with this added number in subset
            subset.pop() # Pop after trying all combinations with subset
            dfs(i + 1, subset, total) # Iterate to next element to try combinations with
        
        dfs(0, [], 0)

        return res
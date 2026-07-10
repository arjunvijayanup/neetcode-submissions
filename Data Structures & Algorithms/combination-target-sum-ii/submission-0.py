class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, subset, total):
            
            if total == target: # If target reached
                res.append(subset.copy())
                return
            if total > target or i >= len(candidates): # Out of bounds or total more than target
                return

            # decision include candidates[i]
            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i]) # i + 1 because cannot reuse the same element
            subset.pop()
            # not include candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1] :
                i += 1

            dfs(i + 1, subset, total)
        
        dfs(0, [], 0)

        return res
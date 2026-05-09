class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # My approach
        n = len(nums)
        ans = []
        ans.extend(nums)
        ans.extend(ans)
        
        return ans

        
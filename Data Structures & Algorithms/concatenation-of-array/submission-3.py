class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # neetcode sol
        n = len(nums)
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans

        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        res = []
        perms = self.permute(nums[1:])

        for p in perms:
            """ith element can be added at the end 
            eg: [2,3], 1 can be added 0th, 1st, 2nd 3 positions"""
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, nums[0])
                res.append(pCopy) 
        
        return res
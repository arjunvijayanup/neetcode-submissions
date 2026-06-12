class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uNums = set()
        for num in nums:
            if uNums and num in uNums:
                return num
            uNums.add(num)
    

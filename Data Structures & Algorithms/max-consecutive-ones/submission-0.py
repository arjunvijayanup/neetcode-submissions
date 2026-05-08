class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, current_count = 0, 0
        for num in nums:
            if num==0:
                max_count = max(max_count, current_count)
                current_count = 0
            else:
                current_count += 1
            
        
        return max(max_count, current_count)
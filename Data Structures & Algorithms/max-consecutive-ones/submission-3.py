class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, current_count = 0, 0
        for num in nums:
            current_count+=1 if num==1 else -current_count
            max_count = max(max_count, current_count)
            
        
        return max_count
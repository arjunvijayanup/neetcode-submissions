class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force approach
        output = [1 for i in range(len(nums))] 
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    output[i] *= nums[j]
        
        return output
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in numSet: # If the number is start of sequence
                length = 0
                while (num + length) in numSet: # If the sequence next number is in the set
                    length += 1
                longest = max(length, longest)
        
        return longest




            

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap approach O(n)
        hmap = {}
        for i, val in enumerate(nums):
            hmap[val] = i
        
        for i, val in enumerate(nums):
            diff = target - val
            # hmap[diff]!=i check done for not reusing same index
            if diff in hmap and hmap[diff]!=i:
                return [i, hmap[diff]]
        
        return []
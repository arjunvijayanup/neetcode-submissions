class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}
        for i, val in enumerate(numbers):
            hmap[val] = i
        
        for i, val in enumerate(numbers):
            diff = target - val
            if diff in hmap and hmap[diff] > i:
                return [i+1, hmap[diff]+1]
        
        return []
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        hmap = defaultdict()

        # Creating hashmap with numbers:count (key:value)
        for i in range(len(nums)):
            hmap[nums[i]] = 1 + hmap.get(nums[i], 0)

        hmap_final = sorted(hmap.keys(), key=lambda x: hmap[x], reverse=True)
                

        return hmap_final[:k]
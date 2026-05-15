class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        hmap = defaultdict()
        #till index 7 as, if len(nums) == 7 then index must go until 7, not 6
        freq = [[] for i in range(len(nums) + 1)] 

        
        # Creating hashmap with numbers:count (key:value)
        for n in nums:
            hmap[n] = 1 + hmap.get(n, 0)

        # Creating freq table trick count -> number
        for n, c in hmap.items():
            freq[c].append(n)

        res = []
        # Accessing from reverse the freq table
        # len(freq) - 1 as it is the last valid index
        # you do not need 0 count, hence end at index 1
        for i in range(len(freq)-1, 0, -1): 
            # Accessing each number for each freq
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low <= high:
            mid = low + (high - low) // 2
            sumof = [math.ceil(pile / mid) for pile in piles]
            if sum(sumof) <= h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return res
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-num for num in nums]
        heapq.heapify(minHeap)

        while k > 0:
            res = heapq.heappop(minHeap)
            k -= 1
        
        return -res

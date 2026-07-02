class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            x, y = point
            d = x ** 2 + y ** 2
            minHeap.append([d, x, y])
        
        heapq.heapify(minHeap)
        res = []

        while len(res) < k:
            d, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        
        return res
        
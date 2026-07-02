class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            d = point[0] ** 2 + point[1] ** 2
            minHeap.append([d, point[0], point[1]])
        
        heapq.heapify(minHeap)
        res = []

        while len(res) < k:
            p = heapq.heappop(minHeap)
            res.append([p[1], p[2]])
        
        return res
        
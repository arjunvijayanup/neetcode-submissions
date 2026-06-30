class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k: # To decrease the size of heap to only populate k largest nums
            heapq.heappop(self.minHeap) 


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k: # After appending, remove the minimum (to maintain k most largest)
            heapq.heappop(self.minHeap)
        return self.minHeap[0] # Return the kth largest of the heap 

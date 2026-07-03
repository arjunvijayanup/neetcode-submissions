from _heapq import heapify
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-count for count in counts.values()] # Create maxHeap by taking -ve values of counts of each character occurence
        heapq.heapify(maxHeap)

        time = 0 # Initialize time
        q = deque() # queue for storing (-cnt, idletime (time + n))
        

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1 # Decrease count by 1 (or increase in case of maxHeap)
                if cnt: # Append only if cnt is non-zero
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time: # if q still is not nul and current time == idle time of first element in q
                heapq.heappush(maxHeap, q.popleft()[0]) # Pop the first element in heap and Push the updated count in q back to heap

        return time










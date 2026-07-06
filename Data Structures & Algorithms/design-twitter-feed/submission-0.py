class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list) # userId -> [count, tweetId]
        self.followMap = defaultdict(set) # userId -> (followeeId1, followeeId2, ...)
        self.count = 0 # For time 0, -1, -2, ... for minHeap

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId]) 
        self.count -= 1 # Updating count for tracking recent tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        res, minHeap = [], []

        self.followMap[userId].add(userId) # Adding self user to list to see his tweets as well
        for followeeId in self.followMap[userId]: # Iterating though each followee
            if followeeId in self.tweetMap: # Checking if the followee has any tweets
                i = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][i]
                heapq.heappush(minHeap, [count, tweetId, followeeId, i - 1])
            
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, i = heapq.heappop(minHeap) # get latest tweet
            res.append(tweetId)
            if i >= 0: # if folowee have more than one tweet
                count, tweetId = self.tweetMap[followeeId][i]
                heapq.heappush(minHeap, [count, tweetId, followeeId, i - 1])
        
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]: # Remove only if followee already present
            self.followMap[followerId].remove(followeeId)

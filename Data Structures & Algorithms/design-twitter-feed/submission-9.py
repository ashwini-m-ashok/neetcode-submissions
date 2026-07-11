class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweet_map[userId].append((self.time, tweetId))  

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        
        self.follow_map[userId].add(userId)
        followers = self.follow_map[userId]
        
        maxheap = []

        for user_id in followers:
            tweets_size = len(self.tweet_map[user_id])
            tweets = self.tweet_map[user_id]
            if tweets_size>0:
                latest_tweet_time, latest_tweet_id = tweets[tweets_size-1]
                heapq.heappush(maxheap, (-latest_tweet_time,tweets_size-1,latest_tweet_id ,user_id))

        while maxheap:
            neg_time, index, tweet_id, user = heapq.heappop(maxheap)
            res.append(tweet_id)

            if len(res)==10:
                break

            if index-1>=0:
                t, t_id = self.tweet_map[user][index-1]
                heapq.heappush(maxheap, (-t,index-1,t_id ,user))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        

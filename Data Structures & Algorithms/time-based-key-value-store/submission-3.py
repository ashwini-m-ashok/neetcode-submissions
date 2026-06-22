class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''

        list_values = self.store[key]
        n = len(self.store[key])
        l=0
        r=n-1
        res=''


        while l<=r:
            mid = (l+(r-l)//2)
            
            if list_values[mid][0]<=timestamp:                
                l=mid+1
                res=list_values[mid][1]
            else:
                r=mid-1
        #1,4,6,7,8,
        
        return res

        

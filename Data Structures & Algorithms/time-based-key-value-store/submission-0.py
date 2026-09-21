class TimeMap:

    def __init__(self):

        self.store={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.store:
            self.store[key]=[]

        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store:
            return ""

        value=self.store[key]

        low=0
        high=len(value)-1
        ans=""
        while low<=high:

            mid=(low+high)//2

            current_time=value[mid][0]
            current_val=value[mid][1]

            if current_time==timestamp:
                return current_val

            elif current_time<timestamp:

                ans=current_val
                low=mid+1
            else:
                high=mid-1

        return ans

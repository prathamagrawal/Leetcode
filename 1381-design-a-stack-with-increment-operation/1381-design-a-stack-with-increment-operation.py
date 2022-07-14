class CustomStack:

    def __init__(self, maxSize: int):
        self.queue=[]
        self.maxSize=maxSize
        
    def push(self, x: int) -> None:
        if(len(self.queue)<self.maxSize):
            self.queue.append(x)

    def pop(self) -> int:
        if(len(self.queue)>0):
            item=self.queue.pop(-1)
            return item
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if(len(self.queue)>=k):
            for i in range(k):
                self.queue[i]+=val
        else:
            for i in range(len(self.queue)):
                self.queue[i]+=val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
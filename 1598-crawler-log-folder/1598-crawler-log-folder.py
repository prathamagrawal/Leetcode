class Solution:
    def minOperations(self, logs: List[str]) -> int:
        directory=[]
        for i in logs:
            if(i !="../" and i !="./"):
                directory.append(i)
            elif( i =='./'):
                continue
            else:
                if(len(directory)>0):
                    directory.pop()
                else:
                    continue
        
        return len(directory)
        
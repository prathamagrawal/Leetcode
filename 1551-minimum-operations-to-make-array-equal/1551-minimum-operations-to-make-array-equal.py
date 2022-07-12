class Solution:
    def minOperations(self, n: int) -> int:
        nums=[]
        
        for i in range(n):
            nums.append((2*i)+1)
        
        return n * n >> 2
        
        
        
        
        
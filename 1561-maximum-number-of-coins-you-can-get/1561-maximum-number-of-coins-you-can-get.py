class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        n=len(piles)
        
        for i in range(n//3):
            piles.pop(0)
        
        ans=0
        
        for i in range(0,len(piles),2):
            ans+=piles[i]
            
        return ans
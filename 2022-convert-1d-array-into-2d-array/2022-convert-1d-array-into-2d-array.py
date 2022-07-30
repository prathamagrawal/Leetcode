import numpy as np
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans=[]
        if(len(original)!=(m*n)):
            return ans
        else:        
            counter=0
            for i in range(m):
                ans.append(list(original[counter:counter+n]))
                counter+=n
            return ans
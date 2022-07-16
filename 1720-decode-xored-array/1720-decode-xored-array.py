class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result=[]
        result.append(first)
        
        for i in range(len(encoded)):
            result.append(result[i]^encoded[i])
        
        return result
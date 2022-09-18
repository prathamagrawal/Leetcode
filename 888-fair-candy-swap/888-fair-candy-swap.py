class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A) - sum(B))//2
        B=set(B)
        for i in A:
            if i- diff in B:
                return [i,i-diff]
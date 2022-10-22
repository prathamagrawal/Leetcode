class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        lookup = set(nums)
        print(lookup)
        while original in lookup:
            original *= 2
        return original
            
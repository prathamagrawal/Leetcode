class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        result=[]
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                result.append(nums[i])
        return result
            
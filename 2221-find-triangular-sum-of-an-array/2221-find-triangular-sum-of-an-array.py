class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        temp=[]
        
        for i in range(len(nums)-1):
            temp.append((nums[i]+nums[i+1])%10)
        
        return self.triangularSum(temp)
class Solution:
    def minimumSum(self, num: int) -> int:
        num=str(num)
        nums=[]
        for i in num:
            nums.append(i)
        
        nums.sort()
        
        item1=int(nums[0]+nums[2])
        item2=int(nums[1]+nums[3])
        
        return item1+item2
class Solution:
    def romanToInt(self, s: str) -> int:
        nums=[]
        for i in s:
            if(i=='M'):
                nums.append(1000)
            if(i=='D'):
                nums.append(500)
            if(i=='C'):
                nums.append(100)
            if(i=='L'):
                nums.append(50)
            if(i=='X'):
                nums.append(10)
            if(i=='V'):
                nums.append(5)
            if(i=='I'):
                nums.append(1)
              
        print(nums)
        ans=0
        for i in range(len(nums)-1):
            if(nums[i]<nums[i+1]):
                ans-=nums[i]
            else:
                ans+=nums[i]
        
        return ans+nums[len(nums)-1]
            
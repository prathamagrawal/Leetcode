class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for item in nums:
            if(item%2==0):
                even.append(item)
            else:
                odd.append(item)
        for item in odd:
            even.append(item)
        return even
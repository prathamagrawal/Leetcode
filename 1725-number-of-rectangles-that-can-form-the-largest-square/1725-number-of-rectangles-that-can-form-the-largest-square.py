class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxSize=0
        arr=[]
        for item in rectangles:
            temp=min(item[0],item[1])
            arr.append(temp)
            if(maxSize<temp):
                maxSize=temp
            
        print(arr)
        return arr.count(maxSize)
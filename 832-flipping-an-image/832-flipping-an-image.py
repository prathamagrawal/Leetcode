class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result=[]
        for item in image:
            temp=[]
            for j in item:
                if(j==0):
                    temp.insert(0,1)
                else:
                    temp.insert(0,0)
            result.append(temp)
        
        return result
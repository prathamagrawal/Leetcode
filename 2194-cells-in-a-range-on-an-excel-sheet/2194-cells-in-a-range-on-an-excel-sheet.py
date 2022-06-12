class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        col1,col2,r1,r2=s[0],s[3],int(s[1]),int(s[4])

        index1=alphabets.index(col1)
        index2=alphabets.index(col2)

        result=[]

        for i in range(index1,index2+1):
            for j in range(r1,r2+1):
                temp=str(alphabets[i])+str(j)
                result.append(temp)
        return result
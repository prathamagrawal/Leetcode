class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result=[]
        
        for query in queries:
            counter=0
            for point in points:
                temp=math.dist((point[0],point[1]),(query[0],query[1]))
                if(temp<=query[2]):
                    counter+=1
            result.append(counter)
            
        
        return result
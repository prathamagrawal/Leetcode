import numpy
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        data={}
        s=list(s)

        for i in s:
            data[i]=s.count(i)

        values=numpy.array(list(data.values()))

        if(len(numpy.unique(values))==1):
            return True
        else:
            return False
        
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d={}
        for i in range(len(paths)):
            d[paths[i][0]]=paths[i][1]

        keys=list(d.keys())
        values=list(d.values())

        for i in values:
            if (i not in keys):
                return i

        
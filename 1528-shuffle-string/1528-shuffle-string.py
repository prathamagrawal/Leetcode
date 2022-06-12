class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        string=list(s)
        print(string)

        data={}
        for i in range(len(indices)):
            data[indices[i]]=string[i]

        print(data)

        result=""
        for i in sorted(data):
            result+=data[i]
        return result
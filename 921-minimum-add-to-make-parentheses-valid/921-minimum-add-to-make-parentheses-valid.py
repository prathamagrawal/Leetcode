class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        counter=0
        for i in s:
            if(i=='('):
                stack.append("0")
            else:
                if(len(stack)>0):            
                    if(stack[-1]=='0'):
                        stack.pop()
                else:
                    counter+=1
        counter+=len(stack)
        return counter
                    
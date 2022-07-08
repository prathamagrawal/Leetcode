class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        
        for i in s:
            if(i != "#"):
                stack1.append(i)
            else:
                if(len(stack1)>0):
                    stack1.pop()
                else:
                    continue
                
        print(stack1)
        
        for i in t:
            if(i != "#"):
                stack2.append(i)
            else:
                if(len(stack2)>0):
                    stack2.pop()
                else:
                    continue
                
        print(stack2)
        
        return stack1==stack2
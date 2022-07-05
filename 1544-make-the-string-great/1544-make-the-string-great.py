class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        
        for i in s:
            if(len(stack)==0):
                stack.append(i)
                print(stack)
            else:
                item=stack.pop()
                if((ord(item)-ord(i)==-32) or(ord(item)-ord(i)==32) ):
                    continue
                else:
                    stack.append(item)
                    stack.append(i)
                    print(stack)
                    
                    
        return ''.join(map(str,stack))
                
            
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        
        for i in ops:
            if(i == "D"):
                item=stack.pop()
                stack.append(item)
                stack.append(2*item)
                print(stack)
            elif(i == "C"):
                stack.pop()
                print(stack)
            elif(i == "+"):
                item1=stack.pop()                
                item2=stack.pop()
                stack.append(item2)
                stack.append(item1)
                stack.append(item1+item2)
                print(stack)
            else:
                stack.append(int(i))
                print(stack)
        
        return sum(stack)
        
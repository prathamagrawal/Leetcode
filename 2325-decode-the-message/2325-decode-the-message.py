class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        strings='abcdefghijklmnopqrstuvwxyz'
        temp={' ': ' '}
        i=0
        for item in key:
            if item not in temp:
                temp[item]=strings[i]  
                i+=1
               
        return ''.join(temp[item] for item in message)
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations=list()
        
        for word in words:
            code=''
            for i in word:
                code+=morse[ord(i)-ord('a')]
            
            if(code not in transformations):
                transformations.append(code)
                
        return len(transformations)
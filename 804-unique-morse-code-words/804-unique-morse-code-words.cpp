class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        vector <string> morse{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        
        unordered_set <string> transformations;
        
        for(const string& word: words){
            string result;
            for(const char c: word){
                result += morse[c - 'a'];
            }transformations.insert(result);
        }
    
        return transformations.size();
    }
};
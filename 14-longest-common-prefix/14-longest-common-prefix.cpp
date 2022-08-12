class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string temp = strs[0];
        for(int i = 1; i < strs.size(); i++){
            string temp2 = strs[i];
            for(int j = 0; j < temp.size(); j++){
                if(temp[j] != temp2[j]){
                    temp.erase(temp.begin()+j,temp.end());
                }
            }
        }
        return temp;
    }
};
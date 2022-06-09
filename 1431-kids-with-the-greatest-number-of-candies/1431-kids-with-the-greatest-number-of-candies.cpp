class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int x=*max_element(candies.begin(),candies.end());
        vector <bool> result;
        int temp;
        for(int i=0;i<candies.size();i++){
            temp=candies[i]+extraCandies;
            if(temp>=x){
                result.push_back(true);
            }
            else{
                result.push_back(false);
            }
        }
        
        return result;
        
    }
};
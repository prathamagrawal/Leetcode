class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int res=0;
        int temp=0;
        for (int i=0;i<gain.size();i++){
            temp=temp+gain[i];
            if(temp>res){
                res=temp;
            }
        }
        return res;
    }
};
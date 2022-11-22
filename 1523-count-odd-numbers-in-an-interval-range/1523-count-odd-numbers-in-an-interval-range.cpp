class Solution {
public:
    int countOdds(int low, int high) {
        int temp=0;
        for (int i=low;i<high+1;i++){
            if(i%2==1){
                temp++;
            }
        }
        return temp;
    }
};
class Solution {
public:
    int arrangeCoins(int n) {
        int counter=1;
        bool flag=true;
        while(flag){
            if(n>=counter){
                n=n-counter;
                counter+=1;
            }else{
                flag=false;
            }
        }
        return (counter-1);
    }
};
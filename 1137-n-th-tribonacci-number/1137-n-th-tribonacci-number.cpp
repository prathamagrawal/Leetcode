class Solution {
public:
    int tribonacci(int n) {
        long x=0;
        long y=1;
        long z=1;
        long array[n+3];
        long result=x+y+z;
        array[0]=x;
        array[1]=y;
        array[2]=z;
        
        for(int i=3;i<n+3;i++){
            result=x+y+z;
            x=y;
            y=z;
            z=result;
            array[i]=result;
        }
        return array[n];
        
    }
};
class Solution {
public:
    int fib(int n) {
        int x=0;
        int y=1;
        int result=x+y;    
        int array[n+1];
        array[0]=x;
    
        for(int i=1;i<n+1;i++){
            array[i]=result;
            result=x+y;
            x=y;
            y=result;
        }
        return array[n];
    }
};
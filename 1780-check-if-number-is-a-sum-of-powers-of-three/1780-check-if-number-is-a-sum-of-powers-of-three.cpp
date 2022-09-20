class Solution {
public:
    bool checkPowersOfThree(int N) {
        while (N > 0) {
            if (N % 3 == 2) {
                return false;
            }
           N /= 3;
        }
        return true;
    }
};
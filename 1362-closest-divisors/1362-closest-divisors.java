class Solution {
    public int[] closestDivisors(int num) {
        int[] r1 = findDivisors(num + 1);
        int[] r2 = findDivisors(num + 2);
        int d1 = r1[1] - r1[0];
        int d2 = r2[1] - r2[0];
        if (d1 < d2) {
            return r1;
        }
        return r2;
    }
    
    public int[] findDivisors(int n) {
        int div = 1;
        for (int i = (int) Math.sqrt(n); i > 1; i--) {
            if (n % i == 0) {
                div = i;
                break;
            }
        }
        int[] res = new int[2];
        res[0] = div;
        res[1] = n / div;
        return res;
    }
}
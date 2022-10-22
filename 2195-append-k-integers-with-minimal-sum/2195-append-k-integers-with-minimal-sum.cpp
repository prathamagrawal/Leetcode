class Solution {
public:
    long long minimalKSum(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(),nums.end());
		
		// map is used to get the unique values only
        unordered_map<int,int>hash; 
		
        long long sum = 0;
        for(int i=0; i<n; i++){
            if(nums[i] <= k && hash[nums[i]] == 0){ 
                k++;
                sum -= nums[i];
                hash[nums[i]] = 1;
            }
        }
        sum += (long long)k * (k+1) /2;
        return sum;
    }
};
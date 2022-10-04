class Solution {
public:
    int first(vector<int> arr, int x)
    {
        int n=arr.size();
        int low = 0, high = n - 1, res = -1;
        while (low <= high) {
            int mid = (low + high) / 2;

            if (arr[mid] > x)
                high = mid - 1;
            else if (arr[mid] < x)
                low = mid + 1;

            else {
                res = mid;
                high = mid - 1;
            }
        }
        return res;
    }
    int last(vector <int>arr, int x)
    {
        int n=arr.size();
        int low = 0, high = n - 1, res = -1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (arr[mid] > x)
                high = mid - 1;
            else if (arr[mid] < x)
                low = mid + 1;
            else {
                res = mid;
                low = mid + 1;
            }
        }
        return res;
    }
    
    vector<int> searchRange(vector<int>& nums, int target) {
        int f=first(nums,target);
        int l=last(nums,target);
        vector<int> res;
        if(f==-1){
            res.push_back(-1);
            res.push_back(-1);
        }else{
            res.push_back(f);
            res.push_back(l);
        }
        return res;
    }
};
class RecentCounter {
public:
    RecentCounter() {
    }
    
    int ping(int t) {
        requests.push_back(t);
        int lower=t-3000;
        int upper=t;
        int ans=0;
        for (int call:requests){
            if(call<=upper && call>=lower){
                ans++;
            }
        }
        return ans;
    }
    
private:
    vector <int> requests;
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
class OrderedStream {
public:
    OrderedStream(int n): data(n + 1) {}
    
    vector<string> insert(int idKey, string value) {
        data[idKey]=value;
        vector<string>answer;
        if(idKey==pointer){
            while(pointer<data.size() && !data[pointer].empty()){
                answer.push_back(data[pointer++]);
            }
        }
        return answer;
        
    }
private:
    int pointer=1;
    vector<string>data;
};

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream* obj = new OrderedStream(n);
 * vector<string> param_1 = obj->insert(idKey,value);
 */
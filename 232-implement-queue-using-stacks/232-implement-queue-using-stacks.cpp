class MyQueue {
public:
    MyQueue() {
        
    }
    
    void push(int x) {
        queue.push_back(x);
    }
    
    int pop() {
        vector<int>::iterator it;
        it = queue.begin();
        int item=queue[0];
        queue.erase(it);
        return item;
        
        
    }
    
    int peek() {
        return queue[0];
    }
    
    bool empty() {
        if(queue.size()==0){
            return true;
        }
        else{
            return false;
        }
    }
    
private:
    vector<int> queue;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
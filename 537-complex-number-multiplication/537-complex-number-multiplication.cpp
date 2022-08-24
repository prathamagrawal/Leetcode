class Solution {
public:
    string complexNumberMultiply(string num1, string num2) {
        int a,b,c,d,i;
        for(i=0;i<num1.length();i++){
            if(num1[i]=='+'){
                a=stoi(num1.substr(0,i));
                break;
            }
        }
        b=stoi(num1.substr(i + 1,num1.length() - i - 2));
        
        for(i=0;i<num2.length();i++){
            if(num2[i]=='+'){
                c=stoi(num2.substr(0,i));
                break;
            }
        }
        d=stoi(num2.substr(i + 1,num2.length() - i - 2));
        
        int real=a*c-b*d;
        int imag=a*d+b*c;
        
        string output="";
        
        output+=to_string(real);
        output+="+";
        output+=to_string(imag);
        output+="i";
        
        return output;
        
    }
};
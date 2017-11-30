#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

void EDIT_a(string a, set<string> & dis_1){
    string prep[20] = { "of", "to", "in", "for", "with", "on", "at", "by", "from",
        "up", "about", "than", "after", "before", "down", "between", "under", "since",
        "without", "near"};
    
    string b = a;
    string c;
    
    
    for(int i=0; i<20; ++i){
        for (string::size_type it = 0; it< a.length(); ++it){
            if(a[it] == ' '){
                
                a.insert(it+1,prep[i]+"?");
                c=a;
                for(string::size_type k = 0; k< c.length(); ++k){
                    if(c[k] == '?') c[k] = ' ';
                }
                dis_1.insert(c);
                a=b;
            }
            
        }
        
        
    }
    for(set<string>::iterator _it = dis_1.begin(); _it != dis_1.end(); ++_it){
        cout<<*_it<<endl;
    }

    
    
}

int main() {
    set<string> dis_1;
    string a = "angry me";
    EDIT_a(a, dis_1);
    
    return 0;
}
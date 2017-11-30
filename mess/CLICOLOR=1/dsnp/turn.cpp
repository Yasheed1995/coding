#include <iostream>
using namespace std;


int a = 0;
void delay(){for(int i=0;i<50000000;i++);}
int main(){
    char s[4] = { '\\', '|', '/', '-'};
    while(true){
        cout << s[a%4];
        cout.flush();
        delay();
        a++;
        cout << '\b';
    }

}

#include <iostream>

using namespace std;

int main(){
    int ** p3 = new int * ;
    * p3 = new int(20);
    cout << **p3 << endl;
}

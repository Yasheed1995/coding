#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> dd;
    for(int i=0; i<20; ++i){
        dd.push_back(i);
    }

    vector<int>::iterator it = dd.begin();
    cout << "dd.begin: " << *it << endl;
    it++;
    cout << "dd[1]: " << *it << endl;
    cout << "if iterator=begin and iterator--" << endl;
    it = dd.begin();
    it --;
    cout << *it << endl;
    it --;
    cout << *it << endl;
    it--;
    cout << *it << endl;

    return 0;
}

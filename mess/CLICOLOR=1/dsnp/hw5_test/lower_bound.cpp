#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int myints[] = {10, 20 , 30, 30, 20, 10, 10, 20};
    vector<int> v(myints, myints+8);

    sort(v.begin(), v.end());

    vector<int>::iterator low;

    low = lower_bound(v.begin(), v.end(), 20);

    cout << "lower_bound at position " << (low - v.begin()) << endl;

    return 0;
}

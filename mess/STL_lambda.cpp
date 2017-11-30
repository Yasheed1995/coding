#include <iostream>
#include <numeric>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    std::vector<int> V(10);

    std::iota(V.begin(), V.end(), 1);

    std::cout << "Original data: " << endl;
    std::for_each(V.begin(), V.end(), [](auto i){ std::cout << i << "  "; });
    std::cout << std::endl;

    std::sort(V.begin(), V.end(), [](auto i, auto j){ return i>j; });
    
    
    std::for_each(V.begin(), V.end(), [](auto i){ std::cout << i << "  "; });
    
    return 0;

}

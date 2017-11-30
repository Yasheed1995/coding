#include <iostream>
#include <cstdio>

using namespace std;
cout << "enter n"<<endl;
int n;
cin>>n;
void print_array(double pary[][]){
	double array_length=n;

	for (int i=0; i<array_length; i++){
		for (int j=0; j<array_length; j++){
			printf("\t%d",pary[i][j]);
		}
		printf("\n");
	}

}
int main(){
	double A[3][5] = {{1,2,3,4,5},
					{2,3,4,5,6},
					{3,4,5,6,7}
				};
	print_array(A);

	return 0;
}
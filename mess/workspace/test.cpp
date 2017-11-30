// basic file operations 
#include <iostream>
#include <fstream>
using namespace std;

int main(void){
	string line;
	ifstream myfile ("example_1.txt");
	if (myfile.is_open())
	{
		while (getline (myfile,line))
		{
			cout << line << '\n';
		}
		myfile.close();
	}
	else cout << "unable to open file";

}
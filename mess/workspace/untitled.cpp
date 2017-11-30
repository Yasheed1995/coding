#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int main(){
int uid, iid, result, timestamp;

vector<User> v;
while(myfile >> uid >> iid >> result >> timestamp) {
User user;
user.UserId = uid;
user.ItemId = iid;
user.result = result;
user.Unix_timestamp = timestamp;
v.push_back(user);
}
}
/*ifstream myfile( "/tmp2/KDDCUP2012/track1/rec_log_train.txt", "r");
if(myfile){
	// 
	while (getline(myfile,v)){
		myfile.read(v.UserId, sizeof(int));
		myfile.read(v.Itemid, sizeof(int));
		myfile.read(v.Result, sizeof(int));
		myfile.read(v.Unix_timestamp, sizeof(int));
	}

}
}*/
/*if (FILE *fp = fopen( "/tmp2/KDDCUP2012/track1/rec log train.txt", "r"))
{
	char buf[1024];
	while (size_t len = fread(buf, 1, sizeof(buf), fp))
		v.insert(v.end(), buf, buf + len);
	fclose(fp);
}*/


int accept(int u, int i, int t){

	return result;
}
int items(int u1, int u2){
	return ;
}
int users(int i1, int i2, int t1, int t2){
	return ;
}
double ratio(int i, int threshold){
	return ;
}
int findtime_item(int i, int Us){
	return ;
}

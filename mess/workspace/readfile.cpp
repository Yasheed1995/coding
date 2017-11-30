#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
void print(int element){
	cout<<element<<'\n';
} 
void printV(vector<int> vec){
    for_each (vec.begin(), vec.end(),    // range
              print);   
}

class User{
public:
	User();
	User(int UserId, int ItemId, int result, int Unix_timestamp);
	int UserId, ItemId, result, Unix_timestamp;
	~User();
};//create a object User to save myfile

vector<User> v;
ifstream myfile;
myfile.open( "/tmp2/KDDCUP2012/track1/rec_log_train.txt",ios::out|ios::in);

int cmp(int x, int y) {return x < y);}
bool cmpU(User u1, User u2){
	if(u1.UserId() != u2.UserId()) return u1.UserId() < u2.UserId();
	if(u1.ItemId() != u2.ItemId()) return u1.ItemId() < u2.ItemId();
	if(u1.Unix_timestamp() != u2.Unix_timestamp()) return u1.Unix_timestamp() < u2.Unix_timestamp();
	if(u1.result() != u2.result()) return u1.result() < u2.result();

}
bool cmpI(User u1, User u2){
	if(u1.ItemId() != u2.ItemId()) return u1.ItemId() < u2.ItemId();
	if(u1.UserId() != u2.UserId()) return u1.UserId() < u2.UserId();
	if(u1.Unix_timestamp() != u2.Unix_timestamp()) return u1.Unix_timestamp() < u2.Unix_timestamp();
	if(u1.result() != u2.result()) return u1.result() < u2.result();

}

bool cmpT(User u1, User u2){
	if(u1.Unix_timestamp() != u2.Unix_timestamp()) return u1.Unix_timestamp() < u2.Unix_timestamp();
	if(u1.UserId() != u2.UserId()) return u1.UserId() < u2.UserId();
	if(u1.ItemId() != u2.ItemId()) return u1.ItemId() < u2.ItemId();
	if(u1.result() != u2.result()) return u1.result() < u2.result();
	
}

void accept(int u, int i, int t){ // v has been sorted by cmpU
	User c1(u,i,1,t);
	vector<User>::Iterator it = lower_bound(v.begin(), v.end(), c1);
	for (it = v.begin(); it != v.end(); ++it){
		if ((it->UserId == u)&&(it->ItemId == i)&&(it->Unix_timestamp == t))
			cout << it->result << endl;
	}
}

void items(int u1, int u2){// 系統給兩個人的item的交集
	User c1(u1,1,1,1),c2(u2,1,1,1);
	int avoidRepeat = -99;
	vector<User> answer;
	vector<User>::Iterator it_1 = lower_bound(v.begin(), v.end(), c1);
	vector<User>::Iterator it_2 = lower_bound(v.begin(), v.end(), c2);
	while(it_1->UserId == u1 && it_2-> UserId == u2){
		if(it_1->ItemId == it_2->ItemId && it_1->ItemId != avoidRepeat){
			answer.push_back(it_1->ItemId);
			avoidRepeat = it_1->ItemId; // v is sorted, and I just need to set avoidRepeat to the last ItemId
			++it_1;
			++it_2;
		else if(it_1-> ItemId > it_2 -> ItemId) ++it_2;
		else ++it_1;

		}
	}
	sort(answer.begin(), answer.end(), cmp);
	printV(answer); //?
}
void users(int i1, int i2, int t1, int t2){
	User c1(1,i1,1,1);
	User c2(1,i2,1,1);
	int avoidRepeat = -99;
	vector<User> answer;
	vector<User>::Iterator it_1 = lower_bound(v.begin(), v.end(), c1);
	vector<User>::Iterator it_2 = lower_bound(v.begin(), v.end(), c2);

	while(it_1->ItemId == i1 && it_2->ItemId == i2){
		if( it_1->Unix_timestamp < t1 || it_1->Unix_timestamp > t2) // it_1 is not legal
			++it_1;
		if( it_2->Unix_timestamp < t1 || it_2->Unix_timestamp > t2) // it_2 is not legal
			++it_2;
		if( it_1->Unix_timestamp > t1 && it_1->Unix_timestamp < t2 && it_2->Unix_timestamp > t1 && it_2->Unix_timestamp < t2) {// it_1 and it_2 are legal
			if( it_1->UserId == it_2->UserId)
				answer.push_back(it_1->UserId);
			++it_1;
			++it_2; // search for the next user
	}
	}
	sort(answer.begin(), answer.end(), cmp);
	//print
}
/*void users(int i1, int i2, int t1, int i2){

	vector<int> answer;
	for (vector<int>::iterator i = x.begin(); i != x.end(); ++i)
	{
	}
}*/
void ratio(int i, int threshold){
	// first count the #users, and if the times > threshold then append the users to total
	int total, x, ac;
	int numberOfUser = 0;
	vector<int> answer;
	vector<User> it_1 = v.begin();
	for(vector<User>::Iterator i = v.begin(), i != v.end(), ++i){
		if(i->UserId == it_1->UserId){
			x++;
			continue;
		}
		if(x > threshold){
			answer.push_back(i->UserId);
			total++;
		}
		if(i->UserId != it_1->UserId){ // search for the next user
			x = 0;
			it_1->UserId = i->UserId;
		}
	}
	vector<User>::Iterator it_a;
	for(vector<int>::Iterator j = answer.begin(),j != answer.end(), ++j  )

}
void findtime_item(int i, int Us){}
int main(){
int uid, iid, result, timestamp;
while(myfile >> uid >> iid >> result >> timestamp) {//read file
	User user;
	user.UserId() = uid;
	user.ItemId() = iid;
	user.result() = result;
	user.Unix_timestamp() = timestamp;
	v.push_back(user);
	w.push_back(user);
	x.push_back(user);
	}
sort(v.begin(), v.end(), cmpU); // v is sorted by UserId first
sort(w.begin(), w.end(), cmpI); // w is sorted by ItemId first
sort(x.begin(), x.end(), cmpT); // x is sorted by time first
myfile.close();

}























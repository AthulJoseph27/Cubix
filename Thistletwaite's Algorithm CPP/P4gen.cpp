#include<bits/stdc++.h>
#include<fstream>
#include"Cube.h"
using namespace std;

unordered_set<unsigned long long>setOfStates;
vector<char> moves = {'R','L','F','B','U','D'};
Cube cube = Cube({{'B','B','B'},{'B','B','B'},{'B','B','B'}},{{'R','R','R'},{'R','R','R'},{'R','R','R'}},{{'G','G','G'},{'G','G','G'},{'G','G','G'}},{{'O','O','O'},{'O','O','O'},{'O','O','O'}},{{'Y','Y','Y'},{'Y','Y','Y'},{'Y','Y','Y'}},{{'W','W','W'},{'W','W','W'},{'W','W','W'}});
int cnt=0;
fstream sol_file,state_file;

unsigned long long getState(){

	string stateG="",stateO="";
	unsigned long long state_id=0;// G+O

	for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
        	stateG+=cube.left[i][j];

    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            stateG+=cube.right[i][j];

    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            stateO+=cube.front[i][j];

    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            stateO+=cube.back[i][j];

    stateG+=stateO;

    for(int i=0;i<18;i++)
    	if(stateG[i] == 'G') state_id+=(pow(2,i));

    for(int i=18;i<36;i++)
    	if(stateG[i] == 'O') state_id+=(pow(2,i));

    return state_id;

}


void execute(char m){
	if(m == 'R'){
		cube.r();
		cube.r();
	}
	else if(m == 'L'){
		cube.l();
		cube.l();
	}
	else if(m == 'U'){
		cube.u();
		cube.u();
	}
	else if(m == 'D'){
		cube.d();
		cube.d();
	}
	else if(m == 'F'){
		cube.f();
		cube.f();
	}
	else{
		cube.b();
		cube.b();
	}
}

void reverse_execute(char m){

	if(m == 'R'){
		cube.R();
		cube.R();
	}
	else if(m == 'L'){
		cube.L();
		cube.L();
	}
	else if(m == 'U'){
		cube.U();
		cube.U();
	}
	else if(m == 'D'){
		cube.D();
		cube.D();
	}
	else if(m == 'F'){
		cube.F();
		cube.F();
	}
	else{
		cube.B();
		cube.B();
	}

}

void dfs(int depth,string alg){
	if(depth == 2){
		cout<<cnt++<<'\n';
	}
	int size = alg.size();
	unsigned long long tmp;
	if(depth == 15) return;
	for(int i=0;i<6;i++){
		if(alg.back()==moves[i])
			continue;
		execute(moves[i]);
		tmp = getState();
		if(setOfStates.find(tmp) == setOfStates.end()){
			setOfStates.insert(tmp);
			sol_file<<alg+moves[i]<<endl;
			state_file<<tmp<<endl;
		}
		dfs(depth+1,alg+moves[i]);
		reverse_execute(moves[i]);
	}
}

int main(){

	sol_file.open("Phase_4_sol.txt",ios::out);
	state_file.open("Phase_4_states.txt",ios::out);
	dfs(0,"");	
	sol_file.close();
	state_file.close();

	return 0;
}

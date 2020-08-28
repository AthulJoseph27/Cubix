#include <bits/stdc++.h>
#include <fstream>
#include "Cube.h"
// #include "timer.h"
using namespace std;

unordered_set<unsigned long long>setOfStates;
vector<char> moves = {'R','L','F','B','U','D'};
Cube cube = Cube({{'G','G','G'},{'G','G','G'},{'G','G','G'}},{{'X','X','X'},{'X','X','X'},{'X','X','X'}},{{'G','G','G'},{'G','G','G'},{'G','G','G'}},{{'X','X','X'},{'X','X','X'},{'X','X','X'}},{{'X','X','X'},{'X','X','X'},{'X','X','X'}},{{'X','X','X'},{'X','X','X'},{'X','X','X'}});
long cnt=0;
fstream sol_file,state_file;

long long getState(){

	string state = "";
	unsigned long long state_id=0;
	
	for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
        	state+=cube.up[i][j];

    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            state+=cube.left[i][j];

    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            state+=cube.front[i][j];

    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            state+=cube.right[i][j];

    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            state+=cube.down[i][j];

    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            state+=cube.back[i][j];
            

    for(int i=0;i<54;i++)
    	if(state[i]=='G') state_id+=(pow(2,i));

    
        
    return state_id;

}

void execute(char m){
	if(m == 'R') cube.r();
	else if(m == 'L') cube.l();
	else if(m == 'U'){
		cube.u();
		cube.u();
	}
	else if(m == 'D'){
		cube.d();
		cube.d();
	}
	else if(m == 'F') cube.f();
	else cube.b();
}

void reverse_execute(char m){

	if(m == 'R') cube.R();
	else if(m == 'L') cube.L();
	else if(m == 'U'){
		cube.U();
		cube.U();
	}
	else if(m == 'D'){
		cube.D();
		cube.D();
	}
	else if(m == 'F') cube.F();
	else cube.B();

}

void dfs(int depth,string alg){
	cout<<cnt++<<'\r';
	int size = alg.size();
	unsigned long long tmp;
	if(depth == 10) return;
	for(int i=0;i<6;i++){
		if((alg.back() == 'U' && i == 4) || (alg.back() == 'D' && i == 5))
			continue;
		if(size == 3 && alg[size-1] == alg[size-2] && alg[size-3] == alg[size-2] && alg[size-1] == moves[i])
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
	// Timer tim = Timer("Pfheew.....That was one heavy dfs Search.........:)");
	sol_file.open("Phase_2_sol.txt",ios::out);
	state_file.open("Phase_2_states.txt",ios::out);
	dfs(0,"");	
	sol_file.close();
	state_file.close();
	return 0;
}


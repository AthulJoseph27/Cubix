#include <bits/stdc++.h>
#include <fstream>
#include "Cube.h"

using namespace std;

vector<string> sol={};
vector<string>states={};
vector<char> moves = {'R','L','F','B','U','D'};
vector<char> ind_state = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'};
Cube cube = Cube({{'G','G','G'},{'G','G','G'},{'G','G','G'}},{{'X','X','X'},{'X','X','X'},{'X','X','X'}},{{'G','G','G'},{'G','G','G'},{'G','G','G'}},{{'X','X','X'},{'X','X','X'},{'X','X','X'}},{{'X','X','X'},{'X','X','X'},{'X','X','X'}},{{'X','X','X'},{'X','X','X'},{'X','X','X'}});
long cnt=0;
fstream sol_file,state_file;

string getState(){

	string state = "",tmp="";
	// int ct = 0;
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
        if(state[i]=='G')
            tmp+=ind_state[i];
        
    return tmp;

}

void execute(char m){
	if(m == 'R') cube.r();
	else if(m == 'L') cube.l();
	else if(m == 'U') cube.u();
	else if(m == 'D') cube.d();
	else if(m == 'F') cube.f();
	else cube.b();
}

void reverse_execute(char m){

	if(m == 'R') cube.R();
	else if(m == 'L') cube.L();
	else if(m == 'U') cube.U();
	else if(m == 'D') cube.D();
	else if(m == 'F') cube.F();
	else cube.B();

}

void dfs(int depth,string alg){
	cout<<cnt++<<'\r';
	int size = alg.size();
	if(depth == 10) return;
	for(int i=0;i<6;i++){
		if((alg.back() == 'U' && i == 4) || (alg.back() == 'D' && i == 5))
			continue;
		if(size == 3 && alg[size-1] == alg[size-2] && alg[size-3] == alg[size-2] && alg[size-1] == moves[i])
			continue;
		execute(moves[i]);
		sol_file<<alg+moves[i]<<endl;
		state_file<<getState()<<endl;
		dfs(depth+1,alg+moves[i]);
		reverse_execute(moves[i]);
	}
}


int main(){
	sol_file.open("Phase_2_sol.txt",ios::out);
	state_file.open("Phase_2_states.txt",ios::out);
	dfs(0,"");	
	sol_file.close();
	state_file.close();
	return 0;
}


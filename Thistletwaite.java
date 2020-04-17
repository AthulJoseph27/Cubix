import java.io.*;
import java.util.*;
// import java.nio.file.Paths;

class Thistletwaite
{
	static char face[][] ={{'R','R','R'},
					       {'R','R','R'},
					       {'R','R','R'}};

	static char back[][] ={{'O','O','O'},
					       {'O','O','O'},
					       {'O','O','O'}};

	static char left[][] ={{'B','B','B'},
					       {'B','B','B'},
					       {'B','B','B'}};

	static char right[][]={{'G','G','G'},
					       {'G','G','G'},
					       {'G','G','G'}};

	static char up [][]  = {{'Y','Y','Y'},
					        {'Y','Y','Y'},
					        {'Y','Y','Y'}};

	static char down[][] ={{'W','W','W'},
					       {'W','W','W'},
					       {'W','W','W'}};

	static char cube[][]=   {{' ',' ',' ','Y','Y','Y',' ',' ',' '},
			                 {' ',' ',' ','Y','Y','Y',' ',' ',' '},
			                 {' ',' ',' ','Y','Y','Y',' ',' ',' '},
			                 {'B','B','B','R','R','R','G','G','G'},
			                 {'B','B','B','R','R','R','G','G','G'},
			                 {'B','B','B','R','R','R','G','G','G'},               
			                 {' ',' ',' ','W','W','W',' ',' ',' '},
			                 {' ',' ',' ','W','W','W',' ',' ',' '},
			                 {' ',' ',' ','W','W','W',' ',' ',' '},
			                 {' ',' ',' ','O','O','O',' ',' ',' '},
			                 {' ',' ',' ','O','O','O',' ',' ',' '},
			                 {' ',' ',' ','O','O','O',' ',' ',' '}};

	static char moves[] = {'R','L','F','B','U','D'}
	//P1) <R,L,F,B,U,D>
	//P2) <R,L,F,B,U2,D2>
	//P3) <R,L,F2,B2,U2,D2>
	//P4) <R2,L2,F2,B2,U2,D2>
	static String[] p2db,p3db,p4db;

	public static   void R()
	 {   
	       t=cube[0][5];
	       cube[0][5]=cube[3][5];
	       cube[3][5]=cube[6][5];
	       cube[6][5]=cube[9][5];
	       cube[9][5]=t;
	       c=cube[2][5];
	       cube[2][5]=cube[5][5];
	       cube[5][5]=cube[8][5];
	       cube[8][5]=cube[11][5];
	       cube[11][5]=c;
	       d=cube[1][5];
	       cube[1][5]=cube[4][5];
	       cube[4][5]=cube[7][5];
	       cube[7][5]=cube[10][5];
	       cube[10][5]=d;
	       b=cube[3][6];
	       cube[3][6]=cube[5][6];
	       cube[5][6]=cube[5][8];
	       cube[5][8]=cube[3][8];
	       cube[3][8]=b;
	       h=cube[4][6];
	       cube[4][6]=cube[5][7];
	       cube[5][7]=cube[4][8];
	       cube[4][8]=cube[3][7];
	       cube[3][7]=h;

	    }
	public static   void Rr()
	 {
	   t=cube[0][5];
	   cube[0][5]=cube[9][5];
	   cube[9][5]=cube[6][5];
	   cube[6][5]=cube[3][5];
	   cube[3][5]=t;
	   c=cube[1][5];
	   cube[1][5]=cube[10][5];
	   cube[10][5]=cube[7][5];
	   cube[7][5]=cube[4][5];
	   cube[4][5]=c;
	   d=cube[2][5];
	   cube[2][5]=cube[11][5];
	   cube[11][5]=cube[8][5];
	   cube[8][5]=cube[5][5];
	   cube[5][5]=d;
	   b=cube[3][6];
	   cube[3][6]=cube[3][8];
	   cube[3][8]=cube[5][8];
	   cube[5][8]=cube[5][6];
	   cube[5][6]=b;
	   h=cube[3][7];
	   cube[3][7]=cube[4][8];
	   cube[4][8]=cube[5][7];
	   cube[5][7]=cube[4][6];
	   cube[4][6]=h;

	 }
	public static  void F()
	  {
	    t=cube[3][4];
	    cube[3][4]=cube[4][3];
	    cube[4][3]=cube[5][4];
	    cube[5][4]=cube[4][5];
	    cube[4][5]=t;
	    b=cube[3][5];
	    cube[3][5]=cube[3][3];
	    cube[3][3]=cube[5][3];
	    cube[5][3]=cube[5][5];
	    cube[5][5]=b;
	    c=cube[2][4];
	    cube[2][4]=cube[4][2];
	    cube[4][2]=cube[6][4];
	    cube[6][4]=cube[4][6];
	    cube[4][6]=c;
	    d=cube[2][5];
	    cube[2][5]=cube[3][2];
	    cube[3][2]=cube[6][3];
	    cube[6][3]=cube[5][6];
	    cube[5][6]=d;
	    h=cube[2][3];
	    cube[2][3]=cube[5][2];
	    cube[5][2]=cube[6][5];
	    cube[6][5]=cube[3][6];
	    cube[3][6]=h;

	        }
	public static  void Fr()
	    {
	        
	    t=cube[3][4];
	    cube[3][4]=cube[4][5];
	    cube[4][5]=cube[5][4];
	    cube[5][4]=cube[4][3];
	    cube[4][3]=t;
	    b=cube[3][5];
	    cube[3][5]=cube[5][5];
	    cube[5][5]=cube[5][3];
	    cube[5][3]=cube[3][3];
	    cube[3][3]=b;
	    c=cube[2][4];
	    cube[2][4]=cube[4][6];
	    cube[4][6]=cube[6][4];
	    cube[6][4]=cube[4][2];
	    cube[4][2]=c;
	    d=cube[2][5];
	    cube[2][5]=cube[5][6];
	    cube[5][6]=cube[6][3];
	    cube[6][3]=cube[3][2];
	    cube[3][2]=d;
	    h=cube[2][3];
	    cube[2][3]=cube[3][6];
	    cube[3][6]=cube[6][5];
	    cube[6][5]=cube[5][2];
	    cube[5][2]=h;

	        }
	public static  void L()
	    {
	        t=cube[0][3];
	        cube[0][3]=cube[9][3];
	        cube[9][3]=cube[6][3];
	        cube[6][3]=cube[3][3];
	        cube[3][3]=t;
	        c=cube[2][3];
	        cube[2][3]=cube[11][3];
	        cube[11][3]=cube[8][3];
	        cube[8][3]=cube[5][3];
	        cube[5][3]=c;
	        b=cube[1][3];
	        cube[1][3]=cube[10][3];
	        cube[10][3]=cube[7][3];
	        cube[7][3]=cube[4][3];
	        cube[4][3]=b;
	        d=cube[3][0];
	        cube[3][0]=cube[5][0];
	        cube[5][0]=cube[5][2];
	        cube[5][2]=cube[3][2];
	        cube[3][2]=d;
	        h=cube[3][1];
	        cube[3][1]=cube[4][0];
	        cube[4][0]=cube[5][1];
	        cube[5][1]=cube[4][2];
	        cube[4][2]=h;

	        }
	public static  void Lr()
	    {
	        t=cube[0][3];
	        cube[0][3]=cube[3][3];
	        cube[3][3]=cube[6][3];
	        cube[6][3]=cube[9][3];
	        cube[9][3]=t;
	        c=cube[2][3];
	        cube[2][3]=cube[5][3];
	        cube[5][3]=cube[8][3];
	        cube[8][3]=cube[11][3];
	        cube[11][3]=c;
	        b=cube[1][3];
	        cube[1][3]=cube[4][3];
	        cube[4][3]=cube[7][3];
	        cube[7][3]=cube[10][3];
	        cube[10][3]=b;
	        d=cube[3][0];
	        cube[3][0]=cube[3][2];
	        cube[3][2]=cube[5][2];
	        cube[5][2]=cube[5][0];
	        cube[5][0]=d;
	        h=cube[3][1];
	        cube[3][1]=cube[4][2];
	        cube[4][2]=cube[5][1];
	        cube[5][1]=cube[4][0];
	        cube[4][0]=h;

	        }
	public static  void U()
	        {
	          t=cube[3][0];
	          cube[3][0]=cube[3][3];
	          cube[3][3]=cube[3][6];
	          cube[3][6]=cube[11][5];
	          cube[11][5]=t;
	          c=cube[3][2];
	          cube[3][2]=cube[3][5];
	          cube[3][5]=cube[3][8];
	          cube[3][8]=cube[11][3];
	          cube[11][3]=c;
	          b=cube[3][1];
	          cube[3][1]=cube[3][4];
	          cube[3][4]=cube[3][7];
	          cube[3][7]=cube[11][4];
	          cube[11][4]=b;
	          d=cube[2][3];
	          cube[2][3]=cube[2][5];
	          cube[2][5]=cube[0][5];
	          cube[0][5]=cube[0][3];
	          cube[0][3]=d;
	          h=cube[2][4];
	          cube[2][4]=cube[1][5];
	          cube[1][5]=cube[0][4];
	          cube[0][4]=cube[1][3];
	          cube[1][3]=h;

	     }
	public static  void Ur()
	    {
	       t=cube[3][0];
	       cube[3][0]=cube[11][5];
	       cube[11][5]=cube[3][6];
	       cube[3][6]=cube[3][3];
	       cube[3][3]=t;
	       c=cube[3][2];
	       cube[3][2]=cube[11][3];
	       cube[11][3]=cube[3][8];
	       cube[3][8]=cube[3][5];
	       cube[3][5]=c;
	       b=cube[3][1];
	       cube[3][1]=cube[11][4];
	       cube[11][4]=cube[3][7];
	       cube[3][7]=cube[3][4];
	       cube[3][4]=b;
	       d=cube[2][3];
	       cube[2][3]=cube[0][3];
	       cube[0][3]=cube[0][5];
	       cube[0][5]=cube[2][5];
	       cube[2][5]=d;
	       h=cube[2][4];
	       cube[2][4]=cube[1][3];
	       cube[1][3]=cube[0][4];
	       cube[0][4]=cube[1][5];
	       cube[1][5]=h;

	        }
	public static  void B()
	        {
	            b=cube[0][5];
	            cube[0][5]=cube[5][8];
	            cube[5][8]=cube[8][3];
	            cube[8][3]=cube[3][0];
	            cube[3][0]=b;
	            c=cube[0][4];
	            cube[0][4]=cube[4][8];
	            cube[4][8]=cube[8][4];
	            cube[8][4]=cube[4][0];
	            cube[4][0]=c;
	            d=cube[0][3];
	            cube[0][3]=cube[3][8];
	            cube[3][8]=cube[8][5];
	            cube[8][5]=cube[5][0];
	            cube[5][0]=d;
	            t=cube[9][4];
	            cube[9][4]=cube[10][3];
	            cube[10][3]=cube[11][4];
	            cube[11][4]=cube[10][5];
	            cube[10][5]=t;
	            h=cube[9][3];
	            cube[9][3]=cube[11][3];
	            cube[11][3]=cube[11][5];
	            cube[11][5]=cube[9][5];
	            cube[9][5]=h;

	        }
	public static  void Br()
	    {
	            b=cube[0][5];
	            cube[0][5]=cube[3][0];
	            cube[3][0]=cube[8][3];
	            cube[8][3]=cube[5][8];
	            cube[5][8]=b;
	            c=cube[0][4];
	            cube[0][4]=cube[4][0];
	            cube[4][0]=cube[8][4];
	            cube[8][4]=cube[4][8];
	            cube[4][8]=c;
	            d=cube[0][3];
	            cube[0][3]=cube[5][0];
	            cube[5][0]=cube[8][5];
	            cube[8][5]=cube[3][8];
	            cube[3][8]=d;
	            t=cube[9][4];
	            cube[9][4]=cube[10][5];
	            cube[10][5]=cube[11][4];
	            cube[11][4]=cube[10][3];
	            cube[10][3]=t;
	            h=cube[9][3];
	            cube[9][3]=cube[9][5];
	            cube[9][5]=cube[11][5];
	            cube[11][5]=cube[11][3];
	            cube[11][3]=h;

	    }
	public static  void D()
	    {
	       t=cube[5][0];
	       cube[5][0]=cube[9][5];
	       cube[9][5]=cube[5][6];
	       cube[5][6]=cube[5][3];
	       cube[5][3]=t;
	       c=cube[5][2];
	       cube[5][2]=cube[9][3];
	       cube[9][3]=cube[5][8];
	       cube[5][8]=cube[5][5];
	       cube[5][5]=c;
	       b=cube[5][1];
	       cube[5][1]=cube[9][4];
	       cube[9][4]=cube[5][7];
	       cube[5][7]=cube[5][4];
	       cube[5][4]=b;
	       d=cube[6][3];
	       cube[6][3]=cube[8][3];
	       cube[8][3]=cube[8][5];
	       cube[8][5]=cube[6][5];
	       cube[6][5]=d;
	       h=cube[6][4];
	       cube[6][4]=cube[7][3];
	       cube[7][3]=cube[8][4];
	       cube[8][4]=cube[7][5];
	       cube[7][5]=h;
	       
	    }  
	public static  void Dr()
	 {
		 t=cube[5][0];
		 cube[5][0]=cube[5][3];
		 cube[5][3]=cube[5][6];
		 cube[5][6]=cube[9][5];
		 cube[9][5]=t;
		 c=cube[5][2];
		 cube[5][2]=cube[5][5];
		 cube[5][5]=cube[5][8];
		 cube[5][8]=cube[9][3];
		 cube[9][3]=c;
		 b=cube[5][1];
		 cube[5][1]=cube[5][4];
		 cube[5][4]=cube[5][7];
		 cube[5][7]=cube[9][4];
		 cube[9][4]=b;
		 d=cube[6][3];
		 cube[6][3]=cube[6][5];
		 cube[6][5]=cube[8][5];
		 cube[8][5]=cube[8][3];
		 cube[8][3]=d;
		 h=cube[6][4];
		 cube[6][4]=cube[7][5];
		 cube[7][5]=cube[8][4];
		 cube[8][4]=cube[7][3];
		 cube[7][3]=h;

	    } 
	public static void split_into_face()
		{
				int i,j;
				for(i=0;i<3;i++)
			        for(j=3;j<6;j++)
			            up[i][j-3] = cube[i][j];

			    for(i=6;i<9;i++)
			        for(j=3;j<6;j++)
			            down[i-6][j-3] = cube[i][j];

			    for(i=3;i<6;i++)
			        for(j=6;j<9;j++)
			            right[i-3][j-6] = cube[i][j];

			    for(i=3;i<6;i++)
			        for(j=0;j<3;j++)
			            left[i-3][j] = cube[i][j];

			    for(i=9;i<12;i++)
			        for(j=3;j<6;j++)
			            back[i-9][j-3] = cube[i][j];

			    for(i=3;i<6;i++)
			        for(j=3;j<6;j++)
			            face[i-3][j-3] = cube[i][j];
		}
	public static boolean IsPhase1Complete()
		{
			int cost = 0,i,j;
			split_into_face();

			  if (up[1][0] == left[1][1])
	            	cost +=1;
		      else if(up[1][2] == left[1][1])
		            cost +=1;
		      else if(face[2][1] == left[1][1])
		            cost +=1;
		      else if(face[0][1] == left[1][1])
		            cost +=1;
		      else if(face[1][0] == left[1][1])
		            cost +=1;
		      else if(face[1][2] == left[1][1])
		            cost +=1;
		      else if(back[2][1] == left[1][1])
		            cost +=1;
		      else if(back[0][1] == left[1][1])
		            cost +=1;
		      else if(back[1][0] == left[1][1])
		            cost +=1;
		      else if(back[1][2] == left[1][1])
		            cost +=1;
		      else if(down[1][0] == left[1][1])
		            cost +=1;
		      else if(down[1][2] == left[1][1])
		            cost +=1;

		      else if(up[2][1] == face[1][1])
		            cost +=1;
		      else if(up[0][1] == face[1][1])
		            cost +=1;
		      else if(left[2][1] == face[1][1])
		            cost +=1;
		      else if(left[0][1] == face[1][1])
		            cost +=1;
		      else if(left[1][0] == face[1][1])
		            cost +=1;
		      else if(left[1][2] == face[1][1])
		            cost +=1;
		      else if(right[2][1] == face[1][1])
		            cost +=1;
		      else if(right[0][1] == face[1][1])
		            cost +=1;
		      else if(right[1][0] == face[1][1])
		            cost +=1;
		      else if(right[1][2] == face[1][1])
		            cost +=1;
		      else if(down[0][1] == face[1][1])
		            cost +=1;
		      else if(down[2][1] == face[1][1])
		            cost +=1;

		      else if(up[1][0] == right[1][1])
		            cost +=1;
		      else if(up[1][2] == right[1][1])
		            cost +=1;
		      else if(face[2][1] == right[1][1])
		            cost +=1;
		      else if(face[0][1] == right[1][1])
		            cost +=1;
		      else if(face[1][0] == right[1][1])
		            cost +=1;
		      else if(face[1][2] == right[1][1])
		            cost +=1;
		      else if(back[2][1] == right[1][1])
		            cost +=1;
		      else if(back[0][1] == right[1][1])
		            cost +=1;
		      else if(back[1][0] == right[1][1])
		            cost +=1;
		      else if(back[1][2] == right[1][1])
		            cost +=1;
		      else if(down[1][0] == right[1][1])
		            cost +=1;
		      else if(down[1][2] == right[1][1])
		            cost +=1;

		      else if(up[2][1] == back[1][1])
		            cost +=1;
		      else if(up[0][1] == back[1][1])
		            cost +=1;
		      else if(left[2][1] == back[1][1])
		            cost +=1;
		      else if(left[0][1] == back[1][1])
		            cost +=1;
		      else if(left[1][0] == back[1][1])
		            cost +=1;
		      else if(left[1][2] == back[1][1])
		            cost +=1;
		      else if(right[2][1] == back[1][1])
		            cost +=1;
		      else if(right[0][1] == back[1][1])
		            cost +=1;
		      else if(right[1][0] == back[1][1])
		            cost +=1;
		      else if(right[1][2] == back[1][1])
		            cost +=1;
		      else if(down[0][1] == back[1][1])
		            cost +=1;
		      else if(down[2][1] == back[1][1])
		            cost +=1;

		       if(cost == 0)
		       		return true;
		       else
		       		return false;
		

		}
	public static boolean IsPhase2Complete()
		

	public static boolean IsPhase3Complete()
	{
		int i,j;

		for(i=0;i<3;i++)
			for(j=3;j<6;j++)
				{
					if(cube[i][j] == 'R')
				    	up[i][j-3] ='O';
				    else if(cube[i][j] == 'B')
				    	up[i][j-3] ='G';
				    else if(cube[i][j] == 'Y')
				    	up[i][j-3] ='W';
				    else
				    	up[i][j-3] =cube[i][j];
				}

	    for(i=6;i<9;i++)
	        for(j=3;j<6;j++)
	        {
	        	if(cube[i][j] == 'R')
	        		down[i-6][j-3] = 'O';
	        	else if(cube[i][j] == 'B')
	        		down[i-6][j-3] = 'G';
	        	else if(cube[i][j] == 'Y')
	        		down[i-6][j-3] = 'W';
	        	else
	            	down[i-6][j-3] = cube[i][j];
	        }

	    for(i=3;i<6;i++)
	        for(j=6;j<9;j++)
	        	{
	        		if(cube[i][j] == 'R')
	            		right[i-3][j-6] = 'O';
	            	else if(cube[i][j] == 'B')
	            		right[i-3][j-6] = 'G';
	            	else if(cube[i][j] == 'Y')
	        			right[i-3][j-6] = 'W';
	        		else
	            		right[i-3][j-6] = cube[i][j];
	        	}

	    for(i=3;i<6;i++)
	        for(j=0;j<3;j++)
	        	{
	        		if(cube[i][j] == 'R')
	            		left[i-3][j] = 'O';
	            	else if(cube[i][j] == 'B')
	            		left[i-3][j] = 'G';
	            	else if(cube[i][j] == 'Y')
	        			left[i-3][j] = 'W';
	        		else
	            		left[i-3][j] = cube[i][j];
	        	}

	    for(i=9;i<12;i++)
	        for(j=3;j<6;j++)
	        	{
	        		if(cube[i][j] == 'R')
	            		back[i-9][j-3] = 'O';
	            	else if(cube[i][j] == 'B')
	            		back[i-9][j-3] = 'G';
	            	else if(cube[i][j] == 'Y')
	        			back[i-9][j-3] = 'W';
	        		else
	            		back[i-9][j-3] = cube[i][j];
	        	}
	             

	    for(i=3;i<6;i++)
	        for(j=3;j<6;j++)
	        	{
	        		if(cube[i][j] == 'R')
	            		face[i-3][j-3] = 'O';
	            	else if(cube[i][j] == 'B')
	            		face[i-3][j-3] = 'G';
	            	else if(cube[i][j] == 'Y')
	        			face[i-3][j-3] = 'W';
	        		else
	            		face[i-3][j-3] = cube[i][j];
	        	}

	    
	             
	}
	public static void main(String [] args)throws IOException
	{
		try
		{
			FileInputStream fileIn0 = new FileInputStream("p2db");
			ObjectInputStream in0 = new ObjectInputStream(fileIn0);
			p2db = (String[])in.readObject();
			in0.close();
			fileIn0.close();
		}
		catch(ClassNotFoundException c)
		{
			System.out.println("Phase2 DataBase Not Found!");
			c.printStackTrace();
		}

		try
		{
			FileInputStream fileIn1 = new FileInputStream("p3db");
			ObjectInputStream in1 = new ObjectInputStream(fileIn1);
			p3db = (String[])in1.readObject();
			in1.close();
			fileIn1.close();
		}
		catch(ClassNotFoundException c)
		{
			System.out.println("Phase3 DataBase Not Found!");
			c.printStackTrace();
		}

		try
		{
			FileInputStream fileIn2 = new FileInputStream("p4db");
			ObjectInputStream in2 = new ObjectInputStream(fileIn2);
			p4db = (String[])in2.readObject();
			in2.close();
			fileIn2.close();
		}
		catch(ClassNotFoundException c)
		{
			System.out.println("Phase4 DataBase Not Found!");
			c.printStackTrace();
		}


	}
}
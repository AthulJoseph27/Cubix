import numpy as np
import random
import time
import pickle
from tqdm import tqdm
import Rcube

face =[['R','R','R'],
       ['R','R','R'],
       ['R','R','R']]
back =[['O','O','O'],
       ['O','O','O'],
       ['O','O','O']]
left =[['B','B','B'],
       ['B','B','B'],
       ['B','B','B']]
right=[['G','G','G'],
       ['G','G','G'],
       ['G','G','G']]
up   = [['Y','Y','Y'],
       ['Y','Y','Y'],
       ['Y','Y','Y']]
down =[['W','W','W'],
       ['W','W','W'],
       ['W','W','W']]
cube =   [[' ',' ',' ','Y','Y','Y',' ',' ',' '],
          [' ',' ',' ','Y','Y','Y',' ',' ',' '],
          [' ',' ',' ','Y','Y','Y',' ',' ',' '],
          ['B','B','B','R','R','R','G','G','G'],
          ['B','B','B','R','R','R','G','G','G'],
          ['B','B','B','R','R','R','G','G','G'],               
          [' ',' ',' ','W','W','W',' ',' ',' '],
          [' ',' ',' ','W','W','W',' ',' ',' '],
          [' ',' ',' ','W','W','W',' ',' ',' '],
          [' ',' ',' ','O','O','O',' ',' ',' '],
          [' ',' ',' ','O','O','O',' ',' ',' '],
          [' ',' ',' ','O','O','O',' ',' ',' ']]
cubix = [[' ',' ',' ','Y','Y','Y',' ',' ',' '],
          [' ',' ',' ','Y','Y','Y',' ',' ',' '],
          [' ',' ',' ','Y','Y','Y',' ',' ',' '],
          ['B','B','B','R','R','R','G','G','G'],
          ['B','B','B','R','R','R','G','G','G'],
          ['B','B','B','R','R','R','G','G','G'],               
          [' ',' ',' ','W','W','W',' ',' ',' '],
          [' ',' ',' ','W','W','W',' ',' ',' '],
          [' ',' ',' ','W','W','W',' ',' ',' '],
          [' ',' ',' ','O','O','O',' ',' ',' '],
          [' ',' ',' ','O','O','O',' ',' ',' '],
          [' ',' ',' ','O','O','O',' ',' ',' ']]

moves = ['R','L','F','B','U','D']
movesp1 = ['R()','L()','F()','B()','U()','D()']
# rev_movesp1  = ['r()','l()','f()','b()','u()','d()']

#                                                           #PART2 - U2,D2,F2,B2
movesp2 = ['R()','L()','F()','B()','U2()','D2()']
# rev_movesp2  = ['r()','l()','f()','b()','U2()','D2()']

movesp3 = ['R()','L()','F2()','B2()','U2()','D2()']
# rev_movesp3  = ['r()','l()','F2()','B2()','U2()','D2()']

movesp4 = ['R2()','L2()','F2()','B2()','U2()','D2()']

data_base = []
sol = []
cost_p1 = [0,0,0,0]
cost_p2 = 0
cost_p3 = 0
cost_p4 = 0
p2_moves = 13
p3_temp_state = []
def R():
      global cube
      t=cube[0][5]
      cube[0][5]=cube[3][5]
      cube[3][5]=cube[6][5]
      cube[6][5]=cube[9][5]
      cube[9][5]=t
      t=cube[2][5]
      cube[2][5]=cube[5][5]
      cube[5][5]=cube[8][5]
      cube[8][5]=cube[11][5]
      cube[11][5]=t
      t=cube[1][5]
      cube[1][5]=cube[4][5]
      cube[4][5]=cube[7][5]
      cube[7][5]=cube[10][5]
      cube[10][5]=t
      t=cube[3][6]
      cube[3][6]=cube[5][6]
      cube[5][6]=cube[5][8]
      cube[5][8]=cube[3][8]
      cube[3][8]=t
      t=cube[4][6]
      cube[4][6]=cube[5][7]
      cube[5][7]=cube[4][8]
      cube[4][8]=cube[3][7]
      cube[3][7]=t
def r():
      global cube
      t=cube[0][5]
      cube[0][5]=cube[9][5]
      cube[9][5]=cube[6][5]
      cube[6][5]=cube[3][5]
      cube[3][5]=t
      t=cube[1][5]
      cube[1][5]=cube[10][5]
      cube[10][5]=cube[7][5]
      cube[7][5]=cube[4][5]
      cube[4][5]=t
      t=cube[2][5]
      cube[2][5]=cube[11][5]
      cube[11][5]=cube[8][5]
      cube[8][5]=cube[5][5]
      cube[5][5]=t
      t=cube[3][6]
      cube[3][6]=cube[3][8]
      cube[3][8]=cube[5][8]
      cube[5][8]=cube[5][6]
      cube[5][6]=t
      t=cube[3][7]
      cube[3][7]=cube[4][8]
      cube[4][8]=cube[5][7]
      cube[5][7]=cube[4][6]
      cube[4][6]=t
def F():
      global cube
      t=cube[3][4]
      cube[3][4]=cube[4][3]
      cube[4][3]=cube[5][4]
      cube[5][4]=cube[4][5]
      cube[4][5]=t
      b=cube[3][5]
      cube[3][5]=cube[3][3]
      cube[3][3]=cube[5][3]
      cube[5][3]=cube[5][5]
      cube[5][5]=b
      c=cube[2][4]
      cube[2][4]=cube[4][2]
      cube[4][2]=cube[6][4]
      cube[6][4]=cube[4][6]
      cube[4][6]=c
      d=cube[2][5]
      cube[2][5]=cube[3][2]
      cube[3][2]=cube[6][3]
      cube[6][3]=cube[5][6]
      cube[5][6]=d
      h=cube[2][3]
      cube[2][3]=cube[5][2]
      cube[5][2]=cube[6][5]
      cube[6][5]=cube[3][6]
      cube[3][6]=h
def f():
      global cube
     
      t=cube[3][4]
      cube[3][4]=cube[4][5]
      cube[4][5]=cube[5][4]
      cube[5][4]=cube[4][3]
      cube[4][3]=t
      b=cube[3][5]
      cube[3][5]=cube[5][5]
      cube[5][5]=cube[5][3]
      cube[5][3]=cube[3][3]
      cube[3][3]=b
      c=cube[2][4]
      cube[2][4]=cube[4][6]
      cube[4][6]=cube[6][4]
      cube[6][4]=cube[4][2]
      cube[4][2]=c
      d=cube[2][5]
      cube[2][5]=cube[5][6]
      cube[5][6]=cube[6][3]
      cube[6][3]=cube[3][2]
      cube[3][2]=d
      h=cube[2][3]
      cube[2][3]=cube[3][6]
      cube[3][6]=cube[6][5]
      cube[6][5]=cube[5][2]
      cube[5][2]=h
def L():
      global cube
      t=cube[0][3]
      cube[0][3]=cube[9][3]
      cube[9][3]=cube[6][3]
      cube[6][3]=cube[3][3]
      cube[3][3]=t
      c=cube[2][3]
      cube[2][3]=cube[11][3]
      cube[11][3]=cube[8][3]
      cube[8][3]=cube[5][3]
      cube[5][3]=c
      b=cube[1][3]
      cube[1][3]=cube[10][3]
      cube[10][3]=cube[7][3]
      cube[7][3]=cube[4][3]
      cube[4][3]=b
      d=cube[3][0]
      cube[3][0]=cube[5][0]
      cube[5][0]=cube[5][2]
      cube[5][2]=cube[3][2]
      cube[3][2]=d
      h=cube[3][1]
      cube[3][1]=cube[4][0]
      cube[4][0]=cube[5][1]
      cube[5][1]=cube[4][2]
      cube[4][2]=h
def l():
      global cube
      t=cube[0][3]
      cube[0][3]=cube[3][3]
      cube[3][3]=cube[6][3]
      cube[6][3]=cube[9][3]
      cube[9][3]=t
      c=cube[2][3]
      cube[2][3]=cube[5][3]
      cube[5][3]=cube[8][3]
      cube[8][3]=cube[11][3]
      cube[11][3]=c
      b=cube[1][3]
      cube[1][3]=cube[4][3]
      cube[4][3]=cube[7][3]
      cube[7][3]=cube[10][3]
      cube[10][3]=b
      d=cube[3][0]
      cube[3][0]=cube[3][2]
      cube[3][2]=cube[5][2]
      cube[5][2]=cube[5][0]
      cube[5][0]=d
      h=cube[3][1]
      cube[3][1]=cube[4][2]
      cube[4][2]=cube[5][1]
      cube[5][1]=cube[4][0]
      cube[4][0]=h
def U():
      global cube
      t=cube[3][0]
      cube[3][0]=cube[3][3]
      cube[3][3]=cube[3][6]
      cube[3][6]=cube[11][5]
      cube[11][5]=t
      c=cube[3][2]
      cube[3][2]=cube[3][5]
      cube[3][5]=cube[3][8]
      cube[3][8]=cube[11][3]
      cube[11][3]=c
      b=cube[3][1]
      cube[3][1]=cube[3][4]
      cube[3][4]=cube[3][7]
      cube[3][7]=cube[11][4]
      cube[11][4]=b
      d=cube[2][3]
      cube[2][3]=cube[2][5]
      cube[2][5]=cube[0][5]
      cube[0][5]=cube[0][3]
      cube[0][3]=d
      h=cube[2][4]
      cube[2][4]=cube[1][5]
      cube[1][5]=cube[0][4]
      cube[0][4]=cube[1][3]
      cube[1][3]=h
def u():
      global cube
      t=cube[3][0]
      cube[3][0]=cube[11][5]
      cube[11][5]=cube[3][6]
      cube[3][6]=cube[3][3]
      cube[3][3]=t
      c=cube[3][2]
      cube[3][2]=cube[11][3]
      cube[11][3]=cube[3][8]
      cube[3][8]=cube[3][5]
      cube[3][5]=c
      b=cube[3][1]
      cube[3][1]=cube[11][4]
      cube[11][4]=cube[3][7]
      cube[3][7]=cube[3][4]
      cube[3][4]=b
      d=cube[2][3]
      cube[2][3]=cube[0][3]
      cube[0][3]=cube[0][5]
      cube[0][5]=cube[2][5]
      cube[2][5]=d
      h=cube[2][4]
      cube[2][4]=cube[1][3]
      cube[1][3]=cube[0][4]
      cube[0][4]=cube[1][5]
      cube[1][5]=h
def B():
      global cube
      b=cube[0][5]
      cube[0][5]=cube[5][8]
      cube[5][8]=cube[8][3]
      cube[8][3]=cube[3][0]
      cube[3][0]=b
      c=cube[0][4]
      cube[0][4]=cube[4][8]
      cube[4][8]=cube[8][4]
      cube[8][4]=cube[4][0]
      cube[4][0]=c
      d=cube[0][3]
      cube[0][3]=cube[3][8]
      cube[3][8]=cube[8][5]
      cube[8][5]=cube[5][0]
      cube[5][0]=d
      t=cube[9][4]
      cube[9][4]=cube[10][3]
      cube[10][3]=cube[11][4]
      cube[11][4]=cube[10][5]
      cube[10][5]=t
      h=cube[9][3]
      cube[9][3]=cube[11][3]
      cube[11][3]=cube[11][5]
      cube[11][5]=cube[9][5]
      cube[9][5]=h
def b():
      global cube
      b=cube[0][5]
      cube[0][5]=cube[3][0]
      cube[3][0]=cube[8][3]
      cube[8][3]=cube[5][8]
      cube[5][8]=b
      c=cube[0][4]
      cube[0][4]=cube[4][0]
      cube[4][0]=cube[8][4]
      cube[8][4]=cube[4][8]
      cube[4][8]=c
      d=cube[0][3]
      cube[0][3]=cube[5][0]
      cube[5][0]=cube[8][5]
      cube[8][5]=cube[3][8]
      cube[3][8]=d
      t=cube[9][4]
      cube[9][4]=cube[10][5]
      cube[10][5]=cube[11][4]
      cube[11][4]=cube[10][3]
      cube[10][3]=t
      h=cube[9][3]
      cube[9][3]=cube[9][5]
      cube[9][5]=cube[11][5]
      cube[11][5]=cube[11][3]
      cube[11][3]=h
def D():
      global cube
      t=cube[5][0]
      cube[5][0]=cube[9][5]
      cube[9][5]=cube[5][6]
      cube[5][6]=cube[5][3]
      cube[5][3]=t
      c=cube[5][2]
      cube[5][2]=cube[9][3]
      cube[9][3]=cube[5][8]
      cube[5][8]=cube[5][5]
      cube[5][5]=c
      b=cube[5][1]
      cube[5][1]=cube[9][4]
      cube[9][4]=cube[5][7]
      cube[5][7]=cube[5][4]
      cube[5][4]=b
      d=cube[6][3]
      cube[6][3]=cube[8][3]
      cube[8][3]=cube[8][5]
      cube[8][5]=cube[6][5]
      cube[6][5]=d
      h=cube[6][4]
      cube[6][4]=cube[7][3]
      cube[7][3]=cube[8][4]
      cube[8][4]=cube[7][5]
      cube[7][5]=h
def d():
      global cube
      t=cube[5][0]
      cube[5][0]=cube[5][3]
      cube[5][3]=cube[5][6]
      cube[5][6]=cube[9][5]
      cube[9][5]=t
      c=cube[5][2]
      cube[5][2]=cube[5][5]
      cube[5][5]=cube[5][8]
      cube[5][8]=cube[9][3]
      cube[9][3]=c
      b=cube[5][1]
      cube[5][1]=cube[5][4]
      cube[5][4]=cube[5][7]
      cube[5][7]=cube[9][4]
      cube[9][4]=b
      d=cube[6][3]
      cube[6][3]=cube[6][5]
      cube[6][5]=cube[8][5]
      cube[8][5]=cube[8][3]
      cube[8][3]=d
      h=cube[6][4]
      cube[6][4]=cube[7][5]
      cube[7][5]=cube[8][4]
      cube[8][4]=cube[7][3]
      cube[7][3]=h
def U2():
      U()
      U()
def D2():
      D()
      D()
def F2():
      F()
      F()
def B2():
      B()
      B()
def R2():
	R()
	R()
def L2():
	L()
	L()



def Classic_Cube():
      for i in range(3):
          for j in range(3,6):
              cube[i][j]=up[i][j-3] 

      for i in range(6,9):
          for j in range(3,6):
              cube[i][j]=down[i-6][j-3]

      for i in range(3,6):
          for j in range(6,9):
              cube[i][j]=right[i-3][j-6]

      for i in range(3,6):
          for j in range(3):
              cube[i][j]=left[i-3][j]

      for i in range(9,12):
          for j in range(3,6):
              cube[i][j]=back[i-9][j-3]

      for i in range(3,6):
          for j in range(3,6):
              cube[i][j]=face[i-3][j-3]

def Evaluate_Phase1Cost():
      global cost_p1,up,down,face,right,left,back,cube

      for i in range(4):
            cost_p1[i] = 0

      for i in range(3):
            for j in range(3,6):
                  up[i][j-3] = cube[i][j]

      for i in range(6,9):
            for j in range(3,6):
                  down[i-6][j-3] = cube[i][j]

      for i in range(3,6):
            for j in range(6,9):
                  right[i-3][j-6] = cube[i][j]

      for i in range(3,6):
            for j in range(3):
                  left[i-3][j] = cube[i][j]

      for i in range(9,12):
            for j in range(3,6):
                  back[i-9][j-3] = cube[i][j]

      for i in range(3,6):
            for j in range(3,6):
                  face[i-3][j-3] = cube[i][j]


      if up[1][0] == left[1][1]:
            # print(1)
            cost_p1[0] +=1
      if up[1][2] == left[1][1]:
            # print(2)
            cost_p1[0] +=1
      if face[2][1] == left[1][1]:
            # print(3)
            cost_p1[0] +=1
      if face[0][1] == left[1][1]:
            # print(4)
            cost_p1[0] +=1
      if face[1][0] == left[1][1]:
            # print(5)
            cost_p1[0] +=1
      if face[1][2] == left[1][1]:
            # print(6)
            cost_p1[0] +=1
      if back[2][1] == left[1][1]:
            # print(7)
            cost_p1[0] +=1
      if back[0][1] == left[1][1]:
            # print(8)
            cost_p1[0] +=1
      if back[1][0] == left[1][1]:
            # print(9)
            cost_p1[0] +=1
      if back[1][2] == left[1][1]:
            # print(10)
            cost_p1[0] +=1
      if down[1][0] == left[1][1]:
            # print(11)
            cost_p1[0] +=1
      if down[1][2] == left[1][1]:
            # print(12)
            cost_p1[0] +=1

      if up[2][1] == face[1][1]:
            cost_p1[1] +=1
      if up[0][1] == face[1][1]:
            cost_p1[1] +=1
      if left[2][1] == face[1][1]:
            cost_p1[1] +=1
      if left[0][1] == face[1][1]:
            cost_p1[1] +=1
      if left[1][0] == face[1][1]:
            cost_p1[1] +=1
      if left[1][2] == face[1][1]:
            cost_p1[1] +=1
      if right[2][1] == face[1][1]:
            cost_p1[1] +=1
      if right[0][1] == face[1][1]:
            cost_p1[1] +=1
      if right[1][0] == face[1][1]:
            cost_p1[1] +=1
      if right[1][2] == face[1][1]:
            cost_p1[1] +=1
      if down[0][1] == face[1][1]:
            cost_p1[1] +=1
      if down[2][1] == face[1][1]:
            cost_p1[1] +=1

      if up[1][0] == right[1][1]:
            cost_p1[2] +=1
      if up[1][2] == right[1][1]:
            cost_p1[2] +=1
      if face[2][1] == right[1][1]:
            cost_p1[2] +=1
      if face[0][1] == right[1][1]:
            cost_p1[2] +=1
      if face[1][0] == right[1][1]:
            cost_p1[2] +=1
      if face[1][2] == right[1][1]:
            cost_p1[2] +=1
      if back[2][1] == right[1][1]:
            cost_p1[2] +=1
      if back[0][1] == right[1][1]:
            cost_p1[2] +=1
      if back[1][0] == right[1][1]:
            cost_p1[2] +=1
      if back[1][2] == right[1][1]:
            cost_p1[2] +=1
      if down[1][0] == right[1][1]:
            cost_p1[2] +=1
      if down[1][2] == right[1][1]:
            cost_p1[2] +=1

      if up[2][1] == back[1][1]:
            cost_p1[3] +=1
      if up[0][1] == back[1][1]:
            cost_p1[3] +=1
      if left[2][1] == back[1][1]:
            cost_p1[3] +=1
      if left[0][1] == back[1][1]:
            cost_p1[3] +=1
      if left[1][0] == back[1][1]:
            cost_p1[3] +=1
      if left[1][2] == back[1][1]:
            cost_p1[3] +=1
      if right[2][1] == back[1][1]:
            cost_p1[3] +=1
      if right[0][1] == back[1][1]:
            cost_p1[3] +=1
      if right[1][0] == back[1][1]:
            cost_p1[3] +=1
      if right[1][2] == back[1][1]:
            cost_p1[3] +=1
      if down[0][1] == back[1][1]:
            cost_p1[3] +=1
      if down[2][1] == back[1][1]:
            cost_p1[3] +=1

def Evaluate_Phase2P2Cost():
    global cost_p2,cube,up,down,face,right,left,back

    cost_p2 = 0

    # for k in range(11):
    #     if cube[k][4]  in ('B','G'):
    #         cost_p2+=1

    # count = 0


    for i in range(3,6):
        for j in range(6,9):
            right[i-3][j-6] = cube[i][j]

    for i in range(3,6):
        for j in range(3):
            left[i-3][j] = cube[i][j]

    for i in (left,right):
        for j in range(3):
        	for k in range(3):
        		if i[j][k] != 'B' and i[j][k] !='G':
        			cost_p2+=1
    # cost_p2 = (8-count)

def Evaluate_Phase2P1Cost():
    global face,back,left,right,up,down,cost_p2,cube

    cost_p2 = 0

    for i in range(11):
        if cube[i][4]  in ('B','G'):
            cost_p2+=1

def Evaluate_Phase4Cost():
        global face,back,left,right,up,down,cost_p4,cube 

        cost_p4 = 0
        f =[['R','R','R'],
            ['R','R','R'],
            ['R','R','R']]
        b =[['O','O','O'],
            ['O','O','O'],
            ['O','O','O']]
        l =[['B','B','B'],
            ['B','B','B'],
            ['B','B','B']]
        r=[['G','G','G'],
           ['G','G','G'],
           ['G','G','G']]
        u=[['Y','Y','Y'],
           ['Y','Y','Y'],
           ['Y','Y','Y']]
        d =[['W','W','W'],
            ['W','W','W'],
            ['W','W','W']]

        for i in range(3):
            for j in range(3,6):
                  up[i][j-3] = cube[i][j]

        for i in range(6,9):
            for j in range(3,6):
                  down[i-6][j-3] = cube[i][j]

        for i in range(3,6):
            for j in range(6,9):
                  right[i-3][j-6] = cube[i][j]

        for i in range(3,6):
            for j in range(3):
                  left[i-3][j] = cube[i][j]

        for i in range(9,12):
            for j in range(3,6):
                  back[i-9][j-3] = cube[i][j]

        for i in range(3,6):
            for j in range(3,6):
                  face[i-3][j-3] = cube[i][j]

        if face != f :
            cost_p4+=1
        elif up != u:
            cost_p4+=1
        elif left !=l:
            cost_p4+=1
        elif right !=r:
            cost_p4+=1
        elif back != b:
            cost_p4+=1
        elif down != d:
            cost_p4+=1

def Evaluate_Phase3Cost():
      global face,back,left,right,up,down,cost_p3,cube

      cost_p3 = 0

      for i in range(9):
            if i > 2 and i < 6:
                  if (cube[10][i] == 'Y') or (cube[10][i] == 'W'):
                        cost_p3+=1
            if i not in (1,4,7):
                  if (cube[3][i] == 'Y') or (cube[3][i] == 'W') or (cube[5][i] == 'Y') or (cube[5][i] == 'W'):
                        cost_p3+=1
            if (cube[4][i] == 'Y') or (cube[4][i] == 'W'):
                  cost_p3+=1
      if (cube[11][3] == 'Y') or (cube[11][5] == 'Y') or (cube[11][3] == 'W') or (cube[11][5] == 'W'):
            cost_p3+=1

     

      for i in range(3,6):
            for j in range(6,9):
                  right[i-3][j-6] = cube[i][j]

      for i in range(3,6):
            for j in range(3):
                  left[i-3][j] = cube[i][j]

      for i in range(9,12):
            for j in range(3,6):
                  back[i-9][j-3] = cube[i][j]

      for i in range(3,6):
            for j in range(3,6):
                  face[i-3][j-3] = cube[i][j]

      count = 0
      for k in (left,right):
            for i in range(3):
                  for j in range(3):
                        if k[i][j] == 'B' or k[i][j] == 'G':
                              count+=1
      cost_p3+=(18-count)

      count = 0
      for k in (face,back):
            for i in range(3):
                  for j in range(3):
                        if k[i][j] == 'O' or k[i][j] == 'R':
                              count+=1
      cost_p3+=(18-count)


def phase1_Search():
      global cost_p1,sol,cube

      sol_len = 100
      p1_solution=''
      dbfile = open("phase1_nodes","rb")
      nodes = list(pickle.load(dbfile))
      dbfile.close()
      nodes.insert(0,' ')
      t_cube = [c[:] for c in cube]
      for i in nodes:
            for j in i:
                  if j != ' ':
                        eval(movesp1[moves.index(j)])
            Evaluate_Phase1Cost()

            c = sum(cost_p1)

            if c == 0:
                  p1_solution = i
                  break

            cube = [c[:] for c in t_cube]
                  
            
            
                        
      sol.append(p1_solution)

# def phase2_p1_Search():
#     global p2_moves,sol,cost_p2,cube

#     dbfile = open('Phase2','rb')
#     nodes = list(pickle.load(dbfile))
#     dbfile.close()
#     p2_p1_sol = ''
#     nodes.sort(key=len)
#     nodes.insert(0,' ')

#     t_cube = list(cube)

#     for i in nodes:
#       for j in i:
#             if j != ' ':
#                 eval(movesp2[moves.index(j)])
            
#       Evaluate_Phase2P1Cost()



#       if cost_p2 == 0:
#             p2_p1_sol = i
#             break

               
#       cube = list(t_cube)   
            
        
                        
#     sol.append(p2_p1_sol)
def Check_DataBase4P2():
    global up,down,left,face,right,back,data_base


    # print(np.array(cube))

    for i in range(3): 
        for j in range(3,6):
              up[i][j-3] = cube[i][j]

    for i in range(6,9):
        for j in range(3,6):
              down[i-6][j-3] = cube[i][j]

    for i in range(3,6):
        for j in range(6,9):
              right[i-3][j-6] = cube[i][j]

    for i in range(3,6):
        for j in range(3):
              left[i-3][j] = cube[i][j]

    for i in range(9,12):
        for j in range(3,6):
              back[i-9][j-3] = cube[i][j]

    for i in range(3,6):
        for j in range(3,6):
              face[i-3][j-3] = cube[i][j]

    for i in (left,right,face,back,up,down):
        for j in range(3):
            for k in range(3):
                if i[j][k] in ['R','O','W','Y']:
                    i[j][k] = 'X'
                if i[j][k] == 'B':
                    i[j][k] = 'G'
          

    cur_state = list([up[:],left[:],face[:],right[:],back[:],down[:]])
    cur_state = np.array(cur_state).reshape(1,54)
    cur_state = [list(cur_state[0])]
    cur_state = ''.join(cur_state[0])


    if cur_state in data_base[0]:
        ind = data_base[0].index(cur_state)
        return data_base[1][ind]
    else:
        
        return ' '

def phase2_p2_Search():
    global p2_moves,sol,cost_p2,cube,data_base

    dbfile = open('Phase2_nodes','rb')
    nodes = list(pickle.load(dbfile))
    dbfile.close()
    p2_p2_sol = ''
    nodes.sort(key=len)
    nodes.insert(0,' ')
    with open("P2DataBase_States.txt","r") as file:
        t_states = file.read().splitlines()

    with open("P2DataBase_Solution.txt","r") as file:
        t_sol=file.read().splitlines()
    data_base.append(t_states)
    data_base.append(t_sol)
    t_cube = [c[:] for c in cube]

    for i in range(len(nodes)):
        for j in nodes[i]:
            if j != ' ':
                eval(movesp2[moves.index(j)])
        
        db_sol = Check_DataBase4P2()
        if db_sol != ' ':
          p2_p2_sol = nodes[i]+db_sol
          
          for k in db_sol:
            eval(movesp2[moves.index(k)])
          break
        Evaluate_Phase2P2Cost()



        if cost_p2 == 0:
            p2_p2_sol = nodes[i]
            break

        cube = [c[:] for c in t_cube]
              
            
                        
    sol.append(p2_p2_sol)

def Check_Data_BaseP3():
      global up,down,left,face,right,back,data_base


      # print(np.array(cube))

      for i in range(3): 
            for j in range(3,6):
                  up[i][j-3] = cube[i][j]

      for i in range(6,9):
            for j in range(3,6):
                  down[i-6][j-3] = cube[i][j]

      for i in range(3,6):
            for j in range(6,9):
                  right[i-3][j-6] = cube[i][j]

      for i in range(3,6):
            for j in range(3):
                  left[i-3][j] = cube[i][j]

      for i in range(9,12):
            for j in range(3,6):
                  back[i-9][j-3] = cube[i][j]

      for i in range(3,6):
            for j in range(3,6):
                  face[i-3][j-3] = cube[i][j]

      for i in (left,right,face,back,up,down):
      	for j in range(3):
      		for k in range(3):
      			if i[j][k] == 'R':
      				i[j][k] = 'O'
      			if i[j][k] == 'B':
      				i[j][k] = 'G'
      			if i[j][k] == 'Y':
      				i[j][k] = 'W' 

      cur_state = list([up[:],left[:],face[:],right[:],back[:],down[:]])
      cur_state = np.array(cur_state).reshape(1,54)
      cur_state = [list(cur_state[0])]

      cur_state = ''.join(cur_state[0])
      
      if cur_state in data_base[0]:
            ind = data_base[0].index(cur_state)
            return data_base[1][ind]
      else:
            
            return ' '

def Check_Data_Base4():
    global up,down,left,face,right,back,data_base


    # print(np.array(cube))

    for i in range(3): 
        for j in range(3,6):
              up[i][j-3] = cube[i][j]

    for i in range(6,9):
        for j in range(3,6):
              down[i-6][j-3] = cube[i][j]

    for i in range(3,6):
        for j in range(6,9):
              right[i-3][j-6] = cube[i][j]

    for i in range(3,6):
        for j in range(3):
              left[i-3][j] = cube[i][j]

    for i in range(9,12):
        for j in range(3,6):
              back[i-9][j-3] = cube[i][j]

    for i in range(3,6):
        for j in range(3,6):
              face[i-3][j-3] = cube[i][j]

    cur_state = list([up[:],left[:],face[:],right[:],back[:],down[:]])
    cur_state = np.array(cur_state).reshape(1,54)
    cur_state = list(cur_state[0])
    cur_state = ''.join(cur_state)

    if cur_state in data_base[0]:
        ind = data_base[0].index(cur_state)
        return data_base[1][ind]
    else:
        
        return ' '

def phase3_Search():
      global p2_moves,sol,cost_p3,data_base,cube

      dbfile = open('Phase3_nodes','rb')
      nodes = list(pickle.load(dbfile))
      dbfile.close()
      data_base = []
      p3_sol = ''
      nodes.insert(0,' ')
      nodes.sort(key=len)
      with open("P3DataBase_States.txt","r") as file:
        t_states = file.read().splitlines()

      with open("P3DataBase_Solution.txt","r") as file:
        t_sol=file.read().splitlines()
      data_base.append(t_states)
      data_base.append(t_sol)
      t_cube = [c[:] for c in cube]
      
      for i in range(len(nodes)):
            
            for j in nodes[i]:
                  if j != ' ':
                        eval(movesp3[moves.index(j)])
            
            db_sol = Check_Data_BaseP3()

            if db_sol != ' ':
                  p3_sol = nodes[i]+db_sol
                  
                  for k in db_sol:
                    if k != ' ':
                        if k == 'r':
                            eval('r()')
                        elif k=='l':
                            eval('l()')
                        else:
                            eval(movesp3[moves.index(k)])
                  break
            Evaluate_Phase3Cost()



            if cost_p3 == 0:
                  p3_sol = nodes[i]
                  
                  break

            cube = [c[:] for c in t_cube]     
            
                        
      sol.append(p3_sol)

def phase4_Search():
    global sol,cost_p4,data_base,cube

    data_base =[]
    t_states =[]
    t_sol =[]
    p4_sol = ''
    with open("P4DataBase_States.txt","r") as file:
    	t_states = file.read().splitlines()

    with open("P4DataBase_Solution.txt","r") as file:
    	t_sol=file.read().splitlines()


    
    data_base.append(list(t_states))
    data_base.append(list(t_sol))
    t_states =[]
    t_sol =[]

    dbfile = open("Phase4_nodes","rb")
    nodes = list(pickle.load(dbfile))
    dbfile.close()
    nodes.insert(0,' ')


    

    t_cube = [c[:] for c in cube]

    for i in range(len(nodes)):
        for j in nodes[i]:
              if j != ' ':
                    eval(movesp4[moves.index(j)])
        

        db_sol = Check_Data_Base4()

        

        if db_sol != ' ':
              
              p4_sol = nodes[i]+db_sol
              for k in db_sol:
                    if k != ' ':
                        eval(movesp4[moves.index(k)])
              break

        Evaluate_Phase4Cost()



        if cost_p4 == 0:
              p4_sol = nodes[i]
              
              break

        cube = [c[:] for c in t_cube] 
            
        
                    
    sol.append(p4_sol)




shuffle = input("ENTER SHUFFLE ALGORITHM\n")

for i in shuffle:
    eval(movesp1[moves.index(i)])
cubix = [row[:] for row in cube]
print(np.array(cube))


start = time.perf_counter()
phase1_Search()
print("*"*20,"Phase1 Completed","*"*20)
print(np.array(cube))



# start = time.perf_counter()
# phase2_p1_Search()
# for i in sol[1]:
#       if i != ' ':
#             eval(movesp2[moves.index(i)])
# print(np.array())
# end = time.perf_counter()
# print(end - start,"s")

# cubix = list()

start = time.perf_counter()
phase2_p2_Search()
print("*"*20,"Phase2 Completed","*"*20)
print(np.array(cube))



start = time.perf_counter()
phase3_Search()
print("*"*20,"Phase3 Completed","*"*20)
print(np.array(cube))



start = time.perf_counter()
phase4_Search()
print("*"*20,"Phase4 Completed","*"*20)
print(np.array(cube))

end = time.perf_counter()

send_sol = []
final_sol = ""
len_sol = len(sol[0])
for i in sol[0]:
    final_sol+=i+' '
    send_sol.append(i)
for i in sol[1]:
    len_sol+=1
    if i == 'U':
        final_sol+='U2 '
        send_sol.append('U2')
    elif i =='D':
        final_sol+='D2 '
        send_sol.append('D2')
    else:
        final_sol+=i+' '
        send_sol.append(i)

for i in sol[2]:
    len_sol+=1
    if i == 'U':
        final_sol+='U2 '
        send_sol.append('U2')
    elif i =='D':
        final_sol+='D2 '
        send_sol.append('D2')
    elif i =='F':
        final_sol+='F2 '
        send_sol.append('F2')
    elif i =='B':
        final_sol+='B2 '
        send_sol.append('B2')
    else:
        final_sol+=i+' '
        send_sol.append(i)

for i in sol[3]:
    len_sol+=1
    if i != ' ':
        send_sol.append((i+'2'))
    final_sol += i+'2 '

print("Solution Found in ",end-start,"s")
print("Solution Length = ",len_sol)
print(final_sol)
print("^"*60)
final_sol = ' '+final_sol
Rcube.display_cube(cubix,send_sol)








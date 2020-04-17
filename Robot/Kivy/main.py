import kivy
import cubix_scan
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.config import Config
#from animation import Animation
 
Config.set('kivy', 'exit_on_escape', '0')
Config.set('kivy','window_icon','Screenshot 2019-11-26 at 9.09.18 PM')

Config.set('graphics', 'height', '700') 
Config.set('graphics', 'width', '400') 

cube=[["R","R","R","R","R","R","R","R","R"],["B","B","B","B","B","B","B","B","B"],["O","O","O","O","O","O","O","O","O"],["G","G","G","G","G","G","G","G","G"],["Y","Y","Y","Y","Y","Y","Y","Y","Y"],["W","W","W","W","W","W","W","W","W"]]
#p=[(1290,920),(1290,810),(1290,700),(1400,920),(1400,810),(1400,700),(1510,920),(1510,810),(1510,700)]
p1=[(190,-70),(190,40),(190,150),(80,-70),(80,40),(80,150),(-30,-70),(-30,40),(-30,150)]
p2=[(220,-40),(220,-10),(220,20),(190,-40),(190,-10),(190,20),(160,-40),(160,-10),(160,20)]
p3=[(130,-40),(130,-10),(130,20),(100,-40),(100,-10),(100,20),(70,-40),(70,-10),(70,20)]
p4=[(40,-40),(40,-10),(40,20),(10,-40),(10,-10),(10,20),(-20,-40),(-20,-10),(-20,20)]
p5=[(-50,-40),(-50,-10),(-50,20),(-80,-40),(-80,-10),(-80,20),(-110,-40),(-110,-10),(-110,20)]
p6=[(130,50),(130,80),(130,110),(100,50),(100,80),(100,110),(70,50),(70,80),(70,110)]
p7=[(130,-70),(130,-100),(130,-130),(100,-70),(100,-100),(100,-130),(70,-70),(70,-100),(70,-130)]
count=0
idf=0
sc_c=0
temp=0
width=0
height=0

class P_Display(FloatLayout): 
	def update_(self, *args): 
		self.rect1.pos = (self.center_x-p2[0][0],self.center_y-p2[0][1])
		self.rect2.pos = (self.center_x-p2[1][0],self.center_y-p2[1][1])
		self.rect3.pos = (self.center_x-p2[2][0],self.center_y-p2[2][1])
		self.rect4.pos = (self.center_x-p2[3][0],self.center_y-p2[3][1])
		self.rect5.pos = (self.center_x-p2[4][0],self.center_y-p2[4][1])
		self.rect6.pos = (self.center_x-p2[5][0],self.center_y-p2[5][1])
		self.rect7.pos = (self.center_x-p2[6][0],self.center_y-p2[6][1])
		self.rect8.pos = (self.center_x-p2[7][0],self.center_y-p2[7][1])
		self.rect9.pos = (self.center_x-p2[8][0],self.center_y-p2[8][1])

		self.rect10.pos = (self.center_x-p3[0][0],self.center_y-p3[0][1])
		self.rect11.pos = (self.center_x-p3[1][0],self.center_y-p3[1][1])
		self.rect12.pos = (self.center_x-p3[2][0],self.center_y-p3[2][1])
		self.rect13.pos = (self.center_x-p3[3][0],self.center_y-p3[3][1])
		self.rect14.pos = (self.center_x-p3[4][0],self.center_y-p3[4][1])
		self.rect15.pos = (self.center_x-p3[5][0],self.center_y-p3[5][1])
		self.rect16.pos = (self.center_x-p3[6][0],self.center_y-p3[6][1])
		self.rect17.pos = (self.center_x-p3[7][0],self.center_y-p3[7][1])
		self.rect18.pos = (self.center_x-p3[8][0],self.center_y-p3[8][1])

		self.rect19.pos = (self.center_x-p4[0][0],self.center_y-p4[0][1])
		self.rect20.pos = (self.center_x-p4[1][0],self.center_y-p4[1][1])
		self.rect21.pos = (self.center_x-p4[2][0],self.center_y-p4[2][1])
		self.rect22.pos = (self.center_x-p4[3][0],self.center_y-p4[3][1])
		self.rect23.pos = (self.center_x-p4[4][0],self.center_y-p4[4][1])
		self.rect24.pos = (self.center_x-p4[5][0],self.center_y-p4[5][1])
		self.rect25.pos = (self.center_x-p4[6][0],self.center_y-p4[6][1])
		self.rect26.pos = (self.center_x-p4[7][0],self.center_y-p4[7][1])
		self.rect27.pos = (self.center_x-p4[8][0],self.center_y-p4[8][1])

		self.rect28.pos = (self.center_x-p5[0][0],self.center_y-p5[0][1])
		self.rect29.pos = (self.center_x-p5[1][0],self.center_y-p5[1][1])
		self.rect30.pos = (self.center_x-p5[2][0],self.center_y-p5[2][1])
		self.rect31.pos = (self.center_x-p5[3][0],self.center_y-p5[3][1])
		self.rect32.pos = (self.center_x-p5[4][0],self.center_y-p5[4][1])
		self.rect33.pos = (self.center_x-p5[5][0],self.center_y-p5[5][1])
		self.rect34.pos = (self.center_x-p5[6][0],self.center_y-p5[6][1])
		self.rect35.pos = (self.center_x-p5[7][0],self.center_y-p5[7][1])
		self.rect36.pos = (self.center_x-p5[8][0],self.center_y-p5[8][1])

		self.rect37.pos = (self.center_x-p6[0][0],self.center_y-p6[0][1])
		self.rect38.pos = (self.center_x-p6[1][0],self.center_y-p6[1][1])
		self.rect39.pos = (self.center_x-p6[2][0],self.center_y-p6[2][1])
		self.rect40.pos = (self.center_x-p6[3][0],self.center_y-p6[3][1])
		self.rect41.pos = (self.center_x-p6[4][0],self.center_y-p6[4][1])
		self.rect42.pos = (self.center_x-p6[5][0],self.center_y-p6[5][1])
		self.rect43.pos = (self.center_x-p6[6][0],self.center_y-p6[6][1])
		self.rect44.pos = (self.center_x-p6[7][0],self.center_y-p6[7][1])
		self.rect45.pos = (self.center_x-p6[8][0],self.center_y-p6[8][1])

		self.rect46.pos = (self.center_x-p7[0][0],self.center_y-p7[0][1])
		self.rect47.pos = (self.center_x-p7[1][0],self.center_y-p7[1][1])
		self.rect48.pos = (self.center_x-p7[2][0],self.center_y-p7[2][1])
		self.rect49.pos = (self.center_x-p7[3][0],self.center_y-p7[3][1])
		self.rect50.pos = (self.center_x-p7[4][0],self.center_y-p7[4][1])
		self.rect51.pos = (self.center_x-p7[5][0],self.center_y-p7[5][1])
		self.rect52.pos = (self.center_x-p7[6][0],self.center_y-p7[6][1])
		self.rect53.pos = (self.center_x-p7[7][0],self.center_y-p7[7][1])
		self.rect54.pos = (self.center_x-p7[8][0],self.center_y-p7[8][1])

		self.rect1.size = (25,25)
		self.rect2.size = (25,25)
		self.rect3.size = (25,25)
		self.rect4.size = (25,25)
		self.rect5.size = (25,25)
		self.rect6.size = (25,25)
		self.rect7.size = (25,25)
		self.rect8.size = (25,25)
		self.rect9.size = (25,25)

		self.rect10.size = (25,25)
		self.rect11.size = (25,25)
		self.rect12.size = (25,25)
		self.rect13.size = (25,25)
		self.rect14.size = (25,25)
		self.rect15.size = (25,25)
		self.rect16.size = (25,25)
		self.rect17.size = (25,25)
		self.rect18.size = (25,25)

		self.rect19.size = (25,25)
		self.rect20.size = (25,25)
		self.rect21.size = (25,25)
		self.rect22.size = (25,25)
		self.rect23.size = (25,25)
		self.rect24.size = (25,25)
		self.rect25.size = (25,25)
		self.rect26.size = (25,25)
		self.rect27.size = (25,25)

		self.rect28.size = (25,25)
		self.rect29.size = (25,25)
		self.rect30.size = (25,25)
		self.rect31.size = (25,25)
		self.rect32.size = (25,25)
		self.rect33.size = (25,25)
		self.rect34.size = (25,25)
		self.rect35.size = (25,25)
		self.rect36.size = (25,25)

		self.rect37.size = (25,25)
		self.rect38.size = (25,25)
		self.rect39.size = (25,25)
		self.rect40.size = (25,25)
		self.rect41.size = (25,25)
		self.rect42.size = (25,25)
		self.rect43.size = (25,25)
		self.rect44.size = (25,25)
		self.rect45.size = (25,25)

		self.rect46.size = (25,25)
		self.rect47.size = (25,25)
		self.rect48.size = (25,25)
		self.rect49.size = (25,25)
		self.rect50.size = (25,25)
		self.rect51.size = (25,25)
		self.rect52.size = (25,25)
		self.rect53.size = (25,25)
		self.rect54.size = (25,25)
	close5 = ObjectProperty
	def __init__(self,**kwargs):
		super(P_Display,self).__init__(**kwargs)
		with self.canvas.after:
			for i in range(9):
				if cube[0][i]=='R':
					Color(1,0,0,1,mode="rgba")
					if i==0:
						self.rect1 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==1:
						self.rect2 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==2:
						self.rect3 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==3:
						self.rect4 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==4:
						self.rect5 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==5:
						self.rect6 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==6:
						self.rect7 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==7:
						self.rect8 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==8:
						self.rect9 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
				if cube[0][i]=='G':
					Color(0,1,0,1,mode="rgba")
					if i==0:
						self.rect1 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==1:
						self.rect2 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==2:
						self.rect3 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==3:
						self.rect4 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==4:
						self.rect5 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==5:
						self.rect6 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==6:
						self.rect7 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==7:
						self.rect8 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==8:
						self.rect9 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))

				if cube[0][i]=='B':
					Color(0,0,1,1,mode="rgba")
					if i==0:
						self.rect1 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==1:
						self.rect2 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==2:
						self.rect3 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==3:
						self.rect4 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==4:
						self.rect5 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==5:
						self.rect6 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==6:
						self.rect7 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==7:
						self.rect8 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==8:
						self.rect9 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
				if cube[0][i]=='O':
					Color(1,0.5,0,1,mode="rgba")
					if i==0:
						self.rect1 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==1:
						self.rect2 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==2:
						self.rect3 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==3:
						self.rect4 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==4:
						self.rect5 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==5:
						self.rect6 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==6:
						self.rect7 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==7:
						self.rect8 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==8:
						self.rect9 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
				if cube[0][i]=='W':
					Color(1,1,1,1,mode="rgba")
					if i==0:
						self.rect1 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==1:
						self.rect2 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==2:
						self.rect3 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==3:
						self.rect4 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==4:
						self.rect5 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==5:
						self.rect6 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==6:
						self.rect7 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==7:
						self.rect8 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==8:
						self.rect9 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
				if cube[0][i]=='Y':
					Color(1,1,0,1,mode="rgba")
					if i==0:
						self.rect1 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==1:
						self.rect2 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==2:
						self.rect3 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==3:
						self.rect4 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==4:
						self.rect5 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==5:
						self.rect6 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==6:
						self.rect7 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==7:
						self.rect8 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
					if i==8:
						self.rect9 = Rectangle(pos=(self.center_x-p2[i][0],self.center_y-p2[i][1]),size=(25,25))
	
			for i in range(9):
				if cube[1][i]=='R':
					Color(1,0,0,1,mode="rgba")
					if i==0:
						self.rect10 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==1:
						self.rect11 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==2:
						self.rect12 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==3:
						self.rect13 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==4:
						self.rect14 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==5:
						self.rect15 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==6:
						self.rect16 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==7:
						self.rect17 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==8:
						self.rect18 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
				if cube[1][i]=='G':
					Color(0,1,0,1,mode="rgba")
					if i==0:
						self.rect10 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==1:
						self.rect11 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==2:
						self.rect12 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==3:
						self.rect13 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==4:
						self.rect14 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==5:
						self.rect15 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==6:
						self.rect16 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==7:
						self.rect17 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==8:
						self.rect18 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))

				if cube[1][i]=='B':
					Color(0,0,1,1,mode="rgba")
					if i==0:
						self.rect10 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==1:
						self.rect11 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==2:
						self.rect12 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==3:
						self.rect13 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==4:
						self.rect14 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==5:
						self.rect15 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==6:
						self.rect16 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==7:
						self.rect17 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==8:
						self.rect18 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
				if cube[1][i]=='O':
					Color(1,0.5,0,1,mode="rgba")
					if i==0:
						self.rect10 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==1:
						self.rect11 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==2:
						self.rect12 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==3:
						self.rect13 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==4:
						self.rect14 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==5:
						self.rect15 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==6:
						self.rect16 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==7:
						self.rect17 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==8:
						self.rect18 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
				if cube[1][i]=='W':
					Color(1,1,1,1,mode="rgba")
					if i==0:
						self.rect10 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==1:
						self.rect11 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==2:
						self.rect12 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==3:
						self.rect13 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==4:
						self.rect14 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==5:
						self.rect15 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==6:
						self.rect16 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==7:
						self.rect17 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==8:
						self.rect18 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
				if cube[1][i]=='Y':
					Color(1,1,0,1,mode="rgba")
					if i==0:
						self.rect10 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==1:
						self.rect11 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==2:
						self.rect12 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==3:
						self.rect13 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==4:
						self.rect14 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==5:
						self.rect15 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==6:
						self.rect16 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==7:
						self.rect17 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))
					if i==8:
						self.rect18 = Rectangle(pos=(self.center_x-p3[i][0],self.center_y-p3[i][1]),size=(25,25))

			for i in range(9):
				if cube[2][i]=='R':
					Color(1,0,0,1,mode="rgba")
					if i==0:
						self.rect19 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==1:
						self.rect20 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==2:
						self.rect21 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==3:
						self.rect22 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==4:
						self.rect23 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==5:
						self.rect24 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==6:
						self.rect25 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==7:
						self.rect26 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==8:
						self.rect27 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
				if cube[2][i]=='G':
					Color(0,1,0,1,mode="rgba")
					if i==0:
						self.rect19 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==1:
						self.rect20 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==2:
						self.rect21 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==3:
						self.rect22 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==4:
						self.rect23 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==5:
						self.rect24 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==6:
						self.rect25 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==7:
						self.rect26 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==8:
						self.rect27 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))

				if cube[2][i]=='B':
					Color(0,0,1,1,mode="rgba")
					if i==0:
						self.rect19 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==1:
						self.rect20 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==2:
						self.rect21 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==3:
						self.rect22 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==4:
						self.rect23 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==5:
						self.rect24 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==6:
						self.rect25 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==7:
						self.rect26 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==8:
						self.rect27 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
				if cube[2][i]=='O':
					Color(1,0.5,0,1,mode="rgba")
					if i==0:
						self.rect19 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==1:
						self.rect20 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==2:
						self.rect21 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==3:
						self.rect22 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==4:
						self.rect23 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==5:
						self.rect24 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==6:
						self.rect25 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==7:
						self.rect26 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==8:
						self.rect27 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
				if cube[2][i]=='W':
					Color(1,1,1,1,mode="rgba")
					if i==0:
						self.rect19 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==1:
						self.rect20 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==2:
						self.rect21 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==3:
						self.rect22 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==4:
						self.rect23 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==5:
						self.rect24 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==6:
						self.rect25 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==7:
						self.rect26 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==8:
						self.rect27 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
				if cube[2][i]=='Y':
					Color(1,1,0,1,mode="rgba")
					if i==0:
						self.rect19 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==1:
						self.rect20 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==2:
						self.rect21 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==3:
						self.rect22 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==4:
						self.rect23 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==5:
						self.rect24 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==6:
						self.rect25 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==7:
						self.rect26 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
					if i==8:
						self.rect27 = Rectangle(pos=(self.center_x-p4[i][0],self.center_y-p4[i][1]),size=(25,25))
			for i in range(9):
				if cube[3][i]=='R':
					Color(1,0,0,1,mode="rgba")
					if i==0:
						self.rect28 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==1:
						self.rect29 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==2:
						self.rect30 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==3:
						self.rect31 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==4:
						self.rect32 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==5:
						self.rect33 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==6:
						self.rect34 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==7:
						self.rect35 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==8:
						self.rect36 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
				if cube[3][i]=='G':
					Color(0,1,0,1,mode="rgba")
					if i==0:
						self.rect28 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==1:
						self.rect29 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==2:
						self.rect30 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==3:
						self.rect31 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==4:
						self.rect32 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==5:
						self.rect33 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==6:
						self.rect34 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==7:
						self.rect35 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==8:
						self.rect36 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
				if cube[3][i]=='B':
					Color(0,0,1,1,mode="rgba")
					if i==0:
						self.rect28 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==1:
						self.rect29 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==2:
						self.rect30 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==3:
						self.rect31 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==4:
						self.rect32 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==5:
						self.rect33 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==6:
						self.rect34 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==7:
						self.rect35 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==8:
						self.rect36 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
				if cube[3][i]=='O':
					Color(1,0.5,0,1,mode="rgba")
					if i==0:
						self.rect28 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==1:
						self.rect29 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==2:
						self.rect30 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==3:
						self.rect31 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==4:
						self.rect32 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==5:
						self.rect33 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==6:
						self.rect34 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==7:
						self.rect35 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==8:
						self.rect36 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
				if cube[3][i]=='W':
					Color(1,1,1,1,mode="rgba")
					if i==0:
						self.rect28 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==1:
						self.rect29 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==2:
						self.rect30 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==3:
						self.rect31 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==4:
						self.rect32 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==5:
						self.rect33 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==6:
						self.rect34 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==7:
						self.rect35 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==8:
						self.rect36 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
				if cube[3][i]=='Y':
					Color(1,1,0,1,mode="rgba")
					if i==0:
						self.rect28 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==1:
						self.rect29 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==2:
						self.rect30 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==3:
						self.rect31 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==4:
						self.rect32 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==5:
						self.rect33 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==6:
						self.rect34 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==7:
						self.rect35 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))
					if i==8:
						self.rect36 = Rectangle(pos=(self.center_x-p5[i][0],self.center_y-p5[i][1]),size=(25,25))


			for i in range(9):
				if cube[4][i]=='R':
					Color(1,0,0,1,mode="rgba")
					if i==0:
						self.rect37 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==1:
						self.rect38 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==2:
						self.rect39 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==3:
						self.rect40 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==4:
						self.rect41 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==5:
						self.rect42 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==6:
						self.rect43 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==7:
						self.rect44 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==8:
						self.rect45 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
				if cube[4][i]=='G':
					Color(0,1,0,1,mode="rgba")
					if i==0:
						self.rect37 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==1:
						self.rect38 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==2:
						self.rect39 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==3:
						self.rect40 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==4:
						self.rect41 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==5:
						self.rect42 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==6:
						self.rect43 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==7:
						self.rect44 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==8:
						self.rect45 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
				if cube[4][i]=='B':
					Color(0,0,1,1,mode="rgba")
					if i==0:
						self.rect37 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==1:
						self.rect38 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==2:
						self.rect39 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==3:
						self.rect40 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==4:
						self.rect41 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==5:
						self.rect42 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==6:
						self.rect43 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==7:
						self.rect44 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==8:
						self.rect45 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
				if cube[4][i]=='O':
					Color(1,0.5,0,1,mode="rgba")
					if i==0:
						self.rect37 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==1:
						self.rect38 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==2:
						self.rect39 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==3:
						self.rect40 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==4:
						self.rect41 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==5:
						self.rect42 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==6:
						self.rect43 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==7:
						self.rect44 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==8:
						self.rect45 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
				if cube[4][i]=='W':
					Color(1,1,1,1,mode="rgba")
					if i==0:
						self.rect37 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==1:
						self.rect38 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==2:
						self.rect39 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==3:
						self.rect40 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==4:
						self.rect41 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==5:
						self.rect42 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==6:
						self.rect43 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==7:
						self.rect44 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==8:
						self.rect45 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
				if cube[4][i]=='Y':
					Color(1,1,0,1,mode="rgba")
					if i==0:
						self.rect37 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==1:
						self.rect38 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==2:
						self.rect39 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==3:
						self.rect40 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==4:
						self.rect41 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==5:
						self.rect42 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==6:
						self.rect43 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==7:
						self.rect44 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
					if i==8:
						self.rect45 = Rectangle(pos=(self.center_x-p6[i][0],self.center_y-p6[i][1]),size=(25,25))
			for i in range(9):
				if cube[5][i]=='R':
					Color(1,0,0,1,mode="rgba")
					if i==0:
						self.rect46 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==1:
						self.rect47 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==2:
						self.rect48 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==3:
						self.rect49 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==4:
						self.rect50 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==5:
						self.rect51 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==6:
						self.rect52 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==7:
						self.rect53 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==8:
						self.rect54 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
				if cube[5][i]=='G':
					Color(0,1,0,1,mode="rgba")
					if i==0:
						self.rect46 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==1:
						self.rect47 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==2:
						self.rect48 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==3:
						self.rect49 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==4:
						self.rect50 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==5:
						self.rect51 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==6:
						self.rect52 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==7:
						self.rect53 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==8:
						self.rect54 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
				if cube[5][i]=='B':
					Color(0,0,1,1,mode="rgba")
					if i==0:
						self.rect46 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==1:
						self.rect47 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==2:
						self.rect48 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==3:
						self.rect49 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==4:
						self.rect50 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==5:
						self.rect51 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==6:
						self.rect52 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==7:
						self.rect53 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==8:
						self.rect54 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
				if cube[5][i]=='O':
					Color(1,0.5,0,1,mode="rgba")
					if i==0:
						self.rect46 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==1:
						self.rect47 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==2:
						self.rect48 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==3:
						self.rect49 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==4:
						self.rect50 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==5:
						self.rect51 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==6:
						self.rect52 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==7:
						self.rect53 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==8:
						self.rect54 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
				if cube[5][i]=='W':
					Color(1,1,1,1,mode="rgba")
					if i==0:
						self.rect46 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==1:
						self.rect47 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==2:
						self.rect48 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==3:
						self.rect49 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==4:
						self.rect50 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==5:
						self.rect51 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==6:
						self.rect52 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==7:
						self.rect53 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==8:
						self.rect54 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
				if cube[5][i]=='Y':
					Color(1,1,0,1,mode="rgba")
					if i==0:
						self.rect46 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==1:
						self.rect47 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==2:
						self.rect48 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==3:
						self.rect49 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==4:
						self.rect50 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==5:
						self.rect51 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==6:
						self.rect52 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==7:
						self.rect53 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
					if i==8:
						self.rect54 = Rectangle(pos=(self.center_x-p7[i][0],self.center_y-p7[i][1]),size=(25,25))
			self.bind(pos = self.update_,size=self.update_)	
			
class P3(FloatLayout):
	close4 = ObjectProperty(None)

class PL(FloatLayout):
	pass	

class P2(FloatLayout):
	close3 = ObjectProperty(None)
	def update_rect(self, *args): 
		self.rect1.pos = (self.center_x-p1[0][0],self.center_y-p1[0][1])
		self.rect2.pos = (self.center_x-p1[1][0],self.center_y-p1[1][1])
		self.rect3.pos = (self.center_x-p1[2][0],self.center_y-p1[2][1])
		self.rect4.pos = (self.center_x-p1[3][0],self.center_y-p1[3][1])
		self.rect5.pos = (self.center_x-p1[4][0],self.center_y-p1[4][1])
		self.rect6.pos = (self.center_x-p1[5][0],self.center_y-p1[5][1])
		self.rect7.pos = (self.center_x-p1[6][0],self.center_y-p1[6][1])
		self.rect8.pos = (self.center_x-p1[7][0],self.center_y-p1[7][1])
		self.rect9.pos = (self.center_x-p1[8][0],self.center_y-p1[8][1])

		self.rect1.size = (100,100)
		self.rect2.size = (100,100)
		self.rect3.size = (100,100)
		self.rect4.size = (100,100)
		self.rect5.size = (100,100)
		self.rect6.size = (100,100)
		self.rect7.size = (100,100)
		self.rect8.size = (100,100)
		self.rect9.size = (100,100)
	def __init__(self,**kwargs):
		super(P2,self).__init__(**kwargs)
		with self.canvas:
			for i in range(9):
				if cube[idf][i]=='R':
					Color(1,0,0,1,mode="rgba")
					if i==0:
						self.rect1 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==1:
						self.rect2 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==2:
						self.rect3 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==3:
						self.rect4 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==4:
						self.rect5 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==5:
						self.rect6 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==6:
						self.rect7 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==7:
						self.rect8 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==8:
						self.rect9 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
				if cube[idf][i]=='G':
					Color(0,1,0,1,mode="rgba")
					if i==0:
						self.rect1 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==1:
						self.rect2 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==2:
						self.rect3 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==3:
						self.rect4 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==4:
						self.rect5 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==5:
						self.rect6 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==6:
						self.rect7 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==7:
						self.rect8 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==8:
						self.rect9 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))

				if cube[idf][i]=='B':
					Color(0,0,1,1,mode="rgba")
					if i==0:
						self.rect1 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==1:
						self.rect2 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==2:
						self.rect3 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==3:
						self.rect4 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==4:
						self.rect5 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==5:
						self.rect6 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==6:
						self.rect7 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==7:
						self.rect8 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==8:
						self.rect9 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
				if cube[idf][i]=='O':
					Color(1,0.5,0,1,mode="rgba")
					if i==0:
						self.rect1 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==1:
						self.rect2 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==2:
						self.rect3 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==3:
						self.rect4 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==4:
						self.rect5 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==5:
						self.rect6 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==6:
						self.rect7 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==7:
						self.rect8 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==8:
						self.rect9 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
				if cube[idf][i]=='W':
					Color(1,1,1,1,mode="rgba")
					if i==0:
						self.rect1 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==1:
						self.rect2 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==2:
						self.rect3 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==3:
						self.rect4 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==4:
						self.rect5 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==5:
						self.rect6 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==6:
						self.rect7 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==7:
						self.rect8 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==8:
						self.rect9 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
				if cube[idf][i]=='Y':
					Color(1,1,0,1,mode="rgba")
					if i==0:
						self.rect1 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==1:
						self.rect2 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==2:
						self.rect3 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==3:
						self.rect4 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==4:
						self.rect5 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==5:
						self.rect6 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==6:
						self.rect7 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==7:
						self.rect8 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))
					if i==8:
						self.rect9 = Rectangle(pos=(self.center_x-p1[i][0],self.center_y-p1[i][1]),size=(100,100))

			self.bind(pos = self.update_rect,size=self.update_rect)	

class P(FloatLayout):
	close0 = ObjectProperty(None)

class P1(FloatLayout):
	close1 = ObjectProperty(None)
	def scan1(self):
		global width,height
		global idf
		idf=0
		try:
			cube[0]=cubix_scan.t()
		except:
			show = P()
			popupWindow = Popup(title="Live Feed is not Avaliable!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2))
			popupWindow.open()
			show.close0.bind(on_press=popupWindow.dismiss)

		show = P2()
		popupWindow1 = Popup(title="Face 1 Scanned!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2),auto_dismiss=False)
		popupWindow1.open()
		show.close3.bind(on_press=popupWindow1.dismiss)

	def scan2(self):
		global idf
		idf=1
		try:
			cube[1]=cubix_scan.t()
		except:
			show = P()
			popupWindow = Popup(title="Live Feed is not Avaliable!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2))
			popupWindow.open()
			show.close0.bind(on_press=popupWindow.dismiss)
		show = P2()
		popupWindow1 = Popup(title="Face 2 Scanned!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2),auto_dismiss=False)
		popupWindow1.open()
		show.close3.bind(on_press=popupWindow1.dismiss)
		
	def scan3(self):
		global idf
		idf=2
		try:
			cube[2]=cubix_scan.t()
		except:
			show = P()
			popupWindow = Popup(title="Live Feed is not Avaliable!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2))
			popupWindow.open()
			show.close0.bind(on_press=popupWindow.dismiss)
		show = P2()
		popupWindow1 = Popup(title="Face 3 Scanned!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2),auto_dismiss=False)
		popupWindow1.open()
		show.close3.bind(on_press=popupWindow1.dismiss)
		
	def scan4(self):
		global idf
		idf=3
		try:
			cube[3]=cubix_scan.t()
		except:
			show = P()
			popupWindow = Popup(title="Live Feed is not Avaliable!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2))
			popupWindow.open()
			show.close0.bind(on_press=popupWindow.dismiss)
		show = P2()
		popupWindow1 = Popup(title="Face 4 Scanned!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2),auto_dismiss=False)
		popupWindow1.open()
		show.close3.bind(on_press=popupWindow1.dismiss)
		
	def scan5(self):
		global idf
		idf=4
		try:
			cube[4]=cubix_scan.t()
		except:
			show = P()
			popupWindow = Popup(title="Live Feed is not Avaliable!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2))
			popupWindow.open()
			show.close0.bind(on_press=popupWindow.dismiss)
		show = P2()
		popupWindow1 = Popup(title="Face 5 Scanned!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2),auto_dismiss=False)
		popupWindow1.open()
		show.close3.bind(on_press=popupWindow1.dismiss)
		
	def scan6(self):
		global idf
		idf=5
		try:
			cube[5]=cubix_scan.t()
		except:
			show = P()
			popupWindow = Popup(title="Live Feed is not Avaliable!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2))
			popupWindow.open()
			show.close0.bind(on_press=popupWindow.dismiss)
		show = P2()
		popupWindow1 = Popup(title="Face 6 Scanned!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2),auto_dismiss=False)
		popupWindow1.open()
		show.close3.bind(on_press=popupWindow1.dismiss)

	def submit(self):
		show = P3()
		popupWindow1 = Popup(title="Submitted!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(400,400),auto_dismiss=False)
		popupWindow1.open()
		show.close4.bind(on_press=popupWindow1.dismiss)

	def display(self):
		show = P_Display()
		popupWindow1 = Popup(title="Scan Successful!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2),auto_dismiss=False)
		popupWindow1.open()
		show.close5.bind(on_press=popupWindow1.dismiss)	

class MyGrid(FloatLayout):
	#s_c_n=ObjectProperty(None)
	#if count==2:
			#self.s_c_n=StringProperty("Submit")
	def scan(self):
		#app = App.get_running_app()
		global count,width,height
		global temp
		global sc_c
		error=0
		width=self.width
		height=self.height

		try:
			temp = cubix_scan.t()
			sc_c=1
		except:
			error=1
			show = P()
			popupWindow = Popup(title="Live Feed is not Avaliable!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2))
			popupWindow.open()
			show.close0.bind(on_press=popupWindow.dismiss)

		if count<6:
			show = 	P1()
			if count==0 and error!=1:
				show.scan1()
			elif count==1 and error!=1:
				show.scan2()
			elif count==2 and error!=1:
				show.scan3()
			elif count==3 and error!=1:
				show.scan4()
			elif count==4 and error!=1:
				show.scan5()
			elif count==5 and error!=1:
				show.scan6()
		else:
			show = P1()
			popupWindow = Popup(title="All Face Scanned!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(width/1.1,height/1.2),auto_dismiss=False)
			popupWindow.open()
			show.close1.bind(on_press=popupWindow.dismiss)

	def dis_live(self):
		"""
		show = PL()
		popupWindow = Popup(title=" ",content=show,size_hint=(900,900),size=(width/1.1,height/1.2))
		popupWindow.open()
		"""
		try:
			cubix_scan.display_live()
		except:
			show = P()
			popupWindow = Popup(title="Live Feed is not Avaliable!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(self.width/1.1,self.height/1.2))
			popupWindow.open()
			show.close0.bind(on_press=popupWindow.dismiss)
		"""
		show.bind(on_press=popupWindow.dismiss)
		"""

	def save(self):
		#app = App.get_running_app()
		global count
		global sc_c
		if sc_c==1:
			try:
				cube.append(temp)
				count+=1
				sc_c=0
			except:
				show = P()
				popupWindow = Popup(title="Invalid Command!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(self.width/1.1,self.height/1.2))
				popupWindow.open()
				show.close0.bind(on_press=popupWindow.dismiss)
		else:
			show = P()
			popupWindow = Popup(title="Invalid Command!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(self.width/1.1,self.height/1.2))
			popupWindow.open()
			show.close0.bind(on_press=popupWindow.dismiss)
	
	def delp(self):
		global count
		if count<7 and count>0:
			count-=1
			cube.pop(-1)
		else:
			show = P()
			popupWindow = Popup(title="Invalid Command!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(self.width/1.1,self.height/1.2))
			popupWindow.open()
			show.close0.bind(on_press=popupWindow.dismiss)

	def dis(self):#display button on P
		show = P_Display()
		popupWindow1 = Popup(title="Scanned Cube!",content=show,size_hint=(None,None),pos_hint={"x":0.05,"top":0.9},size=(self.width/1.1,self.height/1.2),auto_dismiss=False)
		popupWindow1.open()
		show.close5.bind(on_press=popupWindow1.dismiss)	
		pass

class Cubix(App):
	change=0
	def build(self):
		return MyGrid()

if __name__ == "__main__":
 Cubix().run()
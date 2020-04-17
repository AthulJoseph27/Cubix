import cv2
import numpy as np

countf=0
np.array(fravg1=[])
np.array(fravg2=[])
np.array(fravg3=[])
np.array(fravg4=[])
np.array(fravg5=[])
np.array(fravg6=[])
np.array(fravg7=[])
np.array(fravg8=[])
np.array(fravg9=[])
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.MOV',fourcc, 20.0, (640,480))


while True:
 np.array(b1=[])
 np.array( b2=[])
 np.array(b3=[])
 np.array(b4=[])
 np.array(b5=[])
 np.array(b6=[])
 np.array(b7=[])
 np.array(b8=[])
 np.array(b9=[])
 countf+=1
 cap = cv2.VideoCapture("http://192.168.43.1:8080/shot.jpg")
 _, frame1 = cap.read()
 frame=cv2.cvtColor(frame1,cv2.COLOR_BGR2HSV)
 hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
 cv2.rectangle(frame1,(100,100),(150,150),(0,0,255),3)
 cv2.rectangle(frame1,(170,100),(220,150),(0,0,255),3)
 cv2.rectangle(frame1,(240,100),(290,150),(0,0,255),3)
 cv2.rectangle(frame1,(100,170),(150,220),(0,0,255),3)
 cv2.rectangle(frame1,(170,170),(220,220),(0,0,255),3)
 cv2.rectangle(frame1,(240,170),(290,220),(0,0,255),3)
 cv2.rectangle(frame1,(100,240),(150,290),(0,0,255),3)
 cv2.rectangle(frame1,(170,240),(220,290),(0,0,255),3)
 cv2.rectangle(frame1,(240,240),(290,290),(0,0,255),3)

 lower_blue=np.array([91,130,133])
 higher_blue=np.array([114,255,255])
 lower_white=np.array([0,10,153])
 higher_white=np.array([117,97,241])
 lower_red=np.array([110,130,112])
 higher_red=np.array([179,255,255])
 lower_green=np.array([20,60,127])
 higher_green=np.array([64,227,200])
 lower_yellow=np.array([20,61,153])
 higher_yellow=np.array([46,255,255])
 lower_orange=np.array([0,115,163])
 higher_orange=np.array([18,255,255])
 mask1=cv2.inRange(hsv,lower_red,higher_red)
 mask2=cv2.inRange(hsv,lower_white,higher_white)
 mask3=cv2.inRange(hsv,lower_yellow,higher_yellow)
 mask4=cv2.inRange(hsv,lower_blue,higher_blue)
 mask5=cv2.inRange(hsv,lower_green,higher_green)
 mask6=cv2.inRange(hsv,lower_orange,higher_orange)

 
 
 result1=cv2.bitwise_and(frame1,frame1,mask=mask1)
 result2=cv2.bitwise_and(frame1,frame1,mask=mask2)
 result3=cv2.bitwise_and(frame1,frame1,mask=mask3)
 result4=cv2.bitwise_and(frame1,frame1,mask=mask4)
 result5=cv2.bitwise_and(frame1,frame1,mask=mask5)
 result6=cv2.bitwise_and(frame1,frame1,mask=mask6)
 median1=cv2.medianBlur(result1,15)
 median2=cv2.medianBlur(result2,15)
 median3=cv2.medianBlur(result3,15)
 median4=cv2.medianBlur(result4,15)
 median5=cv2.medianBlur(result5,15)
 median6=cv2.medianBlur(result6,15)
 if countf>10 and countf<15:
  for i in range(100,150):
   for j in range(100,150):
    b1.append(frame[i,j])
  for i in range(170,220):
   for j in range(100,150):
    b2.append(frame[i,j])
  for i in range(240,290):
   for j in range(100,150):
    b3.append(frame[i,j])
  for i in range(100,150):
   for j in range(170,220):
    b4.append(frame[i,j])
  for i in range(170,220):
   for j in range(170,220):
    b5.append(frame[i,j])
  for i in range(240,290):
   for j in range(170,220):
    b6.append(frame[i,j])
  for i in range(100,150):
   for j in range(240,290):
    b7.append(frame[i,j])
  for i in range(170,220):
   for j in range(240,290):
    b8.append(frame[i,j])
  for i in range(240,290):
   for j in range(240,290):
    b9.append(frame[i,j])
 if countf>10 and countf<30:
  fravg1.append(np.mean(b1,0))
  fravg2.append(np.mean(b2,0))
  fravg3.append(np.mean(b3,0))
  fravg4.append(np.mean(b4,0))
  fravg5.append(np.mean(b5,0))
  fravg6.append(np.mean(b6,0))
  fravg7.append(np.mean(b7,0))
  fravg8.append(np.mean(b8,0))
  fravg9.append(np.mean(b9,0))
 if countf==30:
     fravg1= np.mean(fravg1,0)
     fravg2= np.mean(fravg2,0)
     fravg3= np.mean(fravg3,0)
     fravg4= np.mean(fravg4,0)
     fravg5= np.mean(fravg5,0)
     fravg6= np.mean(fravg6,0)
     fravg7= np.mean(fravg7,0)
     fravg8= np.mean(fravg8,0)
     fravg9= np.mean(fravg9,0)
 cv2.imshow('frame', frame1)
 cv2.imshow('red', result1)
 cv2.imshow('white', result2)
 cv2.imshow('yellow', result3)
 cv2.imshow('blue', result4)
 cv2.imshow('green', result5)
 cv2.imshow('orange', result6)
 
 if countf==30:
  if fravg1[0]>91 and fravg1[0]<114 and fravg1[1]>130 and fravg1[2]>133:
     print("1.blue")
  if fravg2[0]>91 and fravg2[0]<114 and fravg2[1]>130 and fravg2[2]>133:
     print("2.blue")
  if fravg3[0]>91 and fravg3[0]<114 and fravg3[1]>130 and fravg3[2]>133:
     print("3.blue")
  if fravg4[0]>91 and fravg4[0]<114 and fravg4[1]>130 and fravg4[2]>133:
     print("4.blue")
  if fravg5[0]>91 and fravg5[0]<114 and fravg5[1]>130 and fravg5[2]>133:
     print("5.blue")
  if fravg6[0]>91 and fravg6[0]<114 and fravg6[1]>130 and fravg6[2]>133:
     print("6.blue")
  if fravg7[0]>91 and fravg7[0]<114 and fravg7[1]>130 and fravg7[2]>133:
     print("7.blue")
  if fravg8[0]>91 and fravg8[0]<114 and fravg8[1]>130 and fravg8[2]>133:
     print("8.blue")
  if fravg9[0]>91 and fravg9[0]<114 and fravg9[1]>130 and fravg9[2]>133:
     print("9.blue")



  if fravg1[0]>110 and fravg1[0]<179 and fravg1[1]>130 and fravg1[1]<255 and fravg1[2]>112 and fravg1[2]<255:
     print("1.red")
  if fravg2[0]>110 and fravg2[0]<179 and fravg2[1]>130 and fravg2[1]<255 and fravg2[2]>112 and fravg2[2]<255:
     print("2.red")
  if fravg3[0]>110 and fravg3[0]<179 and fravg3[1]>130 and fravg3[1]<255 and  fravg3[2]>112 and fravg3[2]<255:
     print("3.red")
  if fravg4[0]>110 and fravg4[0]<179 and fravg4[1]>130 and fravg4[1]<255 and fravg4[2]>112 and fravg4[2]<255:
     print("4.red")
  if fravg5[0]>110 and fravg5[0]<179 and fravg5[1]>130 and fravg5[1]<255 and fravg5[2]>112 and fravg5[2]<255:
     print("5.red")
  if fravg6[0]>110 and fravg6[0]<179 and fravg6[1]>130 and fravg6[1]<255 and fravg6[2]>112 and fravg6[2]<255:
     print("6.red")
  if fravg7[0]>110 and fravg7[0]<179 and fravg7[1]>130 and fravg7[1]<255 and fravg7[2]>112 and fravg7[2]<255:
     print("7.red")
  if fravg8[0]>110 and fravg8[0]<179 and fravg8[1]>130 and fravg8[1]<255 and fravg8[2]>112 and fravg8[2]<255:
     print("8.red")
  if fravg9[0]>110 and fravg9[0]<179 and fravg9[1]>130 and fravg9[1]<255 and fravg9[2]>112 and fravg9[2]<255:
     print("9.red")
     
  if fravg1[0]>20 and fravg1[0]<64 and fravg1[1]>60 and fravg1[1]<227 and fravg1[2]>127 and fravg1[2]<200:
     print("1.green")
  if fravg2[0]>20 and fravg2[0]<64 and fravg2[1]>60 and fravg2[1]<227 and fravg2[2]>127 and fravg2[2]<200:
     print("2.green")
  if fravg3[0]>20 and fravg3[0]<64 and fravg3[1]>60 and fravg3[1]<227 and fravg3[2]>127 and fravg3[2]<200:
     print("3.green")
  if fravg4[0]>20 and fravg4[0]<64 and fravg4[1]>60 and fravg4[1]<227 and fravg4[2]>127 and fravg4[2]<200:
     print("4.green")
  if fravg5[0]>20 and fravg5[0]<64 and fravg5[1]>60 and fravg5[1]<227 and fravg5[2]>127 and fravg5[2]<200:
     print("5.green")
  if fravg6[0]>20 and fravg6[0]<64 and fravg6[1]>60 and fravg6[1]<227 and fravg6[2]>127 and fravg6[2]<200:
     print("6.green")
  if fravg7[0]>20 and fravg7[0]<64 and fravg7[1]>60 and fravg7[1]<227 and fravg7[2]>127 and fravg7[2]<200:
     print("7.green")
  if fravg8[0]>20 and fravg8[0]<64 and fravg8[1]>60 and fravg8[1]<227 and fravg8[2]>127 and fravg8[2]<200:
     print("8.green")
  if fravg9[0]>20 and fravg9[0]<64 and fravg9[1]>60 and fravg9[1]<227 and fravg9[2]>127 and fravg9[2]<200:
     print("9.green")

  if fravg1[0]>20 and fravg1[0]<64 and fravg1[1]>61 and fravg1[1]<255 and fravg1[2]>153 and fravg1[2]<255:
     print("1.yellow")
  if fravg2[0]>20 and fravg2[0]<46 and fravg2[1]>61 and fravg2[1]<255 and fravg2[2]>153 and fravg2[2]<255:
     print("2.yellow")
  if fravg3[0]>20 and fravg3[0]<46 and fravg3[1]>61 and fravg3[1]<255 and  fravg3[2]>153 and fravg3[2]<255:
     print("3.yellow")
  if fravg4[0]>20 and fravg4[0]<46 and fravg4[1]>61 and fravg4[1]<255 and fravg4[2]>153 and fravg4[2]<255:
     print("4.yellow")
  if fravg5[0]>20 and fravg5[0]<46 and fravg5[1]>61 and fravg5[1]<255 and fravg5[2]>153 and fravg5[2]<255:
     print("5.yellow")
  if fravg6[0]>20 and fravg6[0]<46 and fravg6[1]>61 and fravg6[1]<255 and fravg6[2]>153 and fravg6[2]<255:
     print("6.yellow")
  if fravg7[0]>20 and fravg7[0]<46 and fravg7[1]>61 and fravg7[1]<255 and fravg7[2]>153 and fravg7[2]<255:
     print("7.yellow")
  if fravg8[0]>20 and fravg8[0]<46 and fravg8[1]>61 and fravg8[1]<255 and fravg8[2]>153 and fravg8[2]<255:
     print("8.yellow")
  if fravg9[0]>20 and fravg9[0]<46 and fravg9[1]>61 and fravg9[1]<255 and fravg9[2]>153 and fravg9[2]<255:
     print("9.yellow")

  if fravg1[0]>0 and fravg1[0]<18 and fravg1[1]>115 and fravg1[1]<240 and fravg1[2]>163 and fravg1[2]<255:
     print("1.orange")
  if fravg2[0]>0 and fravg2[0]<18 and fravg2[1]>115 and fravg2[1]<255 and fravg2[2]>163 and fravg2[2]<255:
     print("2.orange")
  if fravg3[0]>0 and fravg3[0]<18 and fravg3[1]>115 and fravg3[1]<255 and  fravg3[2]>163 and fravg3[2]<255:
     print("3.orange")
  if fravg4[0]>0 and fravg4[0]<18 and fravg4[1]>115 and fravg4[1]<255 and fravg4[2]>163 and fravg4[2]<255:
     print("4.orange")
  if fravg5[0]>0 and fravg5[0]<18 and fravg5[1]>115 and fravg5[1]<255 and fravg5[2]>163 and fravg5[2]<255:
     print("5.orange")
  if fravg6[0]>0 and fravg6[0]<18 and fravg6[1]>115 and fravg6[1]<255 and fravg6[2]>163 and fravg6[2]<255:
     print("6.orange")
  if fravg7[0]>0 and fravg7[0]<18 and fravg7[1]>115 and fravg7[1]<255 and fravg7[2]>163 and fravg7[2]<255:
     print("7.orange")
  if fravg8[0]>0 and fravg8[0]<18 and fravg8[1]>115 and fravg8[1]<255 and fravg8[2]>163 and fravg8[2]<255:
     print("8.orange")
  if fravg9[0]>0 and fravg9[0]<18 and fravg9[1]>115 and fravg9[1]<255 and fravg9[2]>163 and fravg9[2]<255:
     print("9.orange")

  if fravg1[0]>0 and fravg1[0]<117 and fravg1[1]>10 and fravg1[1]<97 and fravg1[2]>153 and fravg1[2]<241:
     print("1.white")
  if fravg2[0]>0 and fravg2[0]<117 and fravg2[1]>10 and fravg2[1]<97 and fravg2[2]>153 and fravg2[2]<241:
     print("2.white")
  if fravg3[0]>0 and fravg3[0]<117 and fravg3[1]>10 and fravg3[1]<97 and  fravg3[2]>153 and fravg3[2]<241:
     print("3.white")
  if fravg4[0]>0 and fravg4[0]<117 and fravg4[1]>10 and fravg4[1]<97 and fravg4[2]>153 and fravg4[2]<241:
     print("4.white")
  if fravg5[0]>0 and fravg5[0]<117 and fravg5[1]>10 and fravg5[1]<97 and fravg5[2]>153 and fravg5[2]<241:
     print("5.white")
  if fravg6[0]>0 and fravg6[0]<117 and fravg6[1]>10 and fravg6[1]<97 and fravg6[2]>153 and fravg6[2]<241:
     print("6.white")
  if fravg7[0]>0 and fravg7[0]<117 and fravg7[1]>10 and fravg7[1]<97 and fravg7[2]>153 and fravg7[2]<241:
     print("7.white")
  if fravg8[0]>0 and fravg8[0]<117 and fravg8[1]>10 and fravg8[1]<97 and fravg8[2]>153 and fravg8[2]<241:
     print("8.white")
  if fravg9[0]>0 and fravg9[0]<117 and fravg9[1]>10 and fravg9[1]<97 and fravg9[2]>153 and fravg9[2]<241:
     print("9.white")

 key=cv2.waitKey(1)
 if key == 27:
  break

cap.release()
cv2.destroyAllWindows()


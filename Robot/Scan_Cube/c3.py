import cv2
import numpy as np
countf=0
fravg1=[[0,0,0]]
fravg2=[[0,0,0]]
fravg3=[[0,0,0]]
fravg4=[[0,0,0]]
fravg5=[[0,0,0]]
fravg6=[[0,0,0]]
fravg7=[[0,0,0]]
fravg8=[[0,0,0]]
fravg9=[[0,0,0]]
fravg1=np.array(fravg1,dtype=np.float32)
fravg2=np.array(fravg2,dtype=np.float32)
fravg3=np.array(fravg3,dtype=np.float32)
fravg4=np.array(fravg4,dtype=np.float32)
fravg5=np.array(fravg5,dtype=np.float32)
fravg6=np.array(fravg6,dtype=np.float32)
fravg7=np.array(fravg7,dtype=np.float32)
fravg8=np.array(fravg8,dtype=np.float32)
fravg9=np.array(fravg9,dtype=np.float32)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.MOV',fourcc, 20.0, (640,480))


while True:
   b1=[[0,0,0]]
   b2=[[0,0,0]]
   b3=[[0,0,0]]
   b4=[[0,0,0]]
   b5=[[0,0,0]]
   b6=[[0,0,0]]
   b7=[[0,0,0]]
   b8=[[0,0,0]]
   b9=[[0,0,0]]
   b1=np.array(b1,dtype=np.float32)
   b2=np.array(b2,dtype=np.float32)
   b3=np.array(b3,dtype=np.float32)
   b4=np.array(b4,dtype=np.float32)
   b5=np.array(b5,dtype=np.float32)
   b6=np.array(b6,dtype=np.float32)
   b7=np.array(b7,dtype=np.float32)
   b8=np.array(b8,dtype=np.float32)
   b9=np.array(b9,dtype=np.float32)
  

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
    for i in range(103,147):
     for j in range(103,147):
      b1=np.concatenate((b1,[frame[i,j]]),axis=0)
    for i in range(173,217):
     for j in range(103,147):
      b2=np.concatenate((b2,[frame[i,j]]),axis=0)
    for i in range(243,287):
     for j in range(103,147):
      b3=np.concatenate((b3,[frame[i,j]]),axis=0)
    for i in range(103,147):
     for j in range(173,217):
      b4=np.concatenate((b4,[frame[i,j]]),axis=0)
    for i in range(173,217):
     for j in range(173,217):
      b5=np.concatenate((b5,[frame[i,j]]),axis=0)
    for i in range(243,287):
     for j in range(173,217):
      b6=np.concatenate((b6,[frame[i,j]]),axis=0)
    for i in range(100,150):
     for j in range(243,287):
      b7=np.concatenate((b7,[frame[i,j]]),axis=0)
    for i in range(173,217):
     for j in range(243,287):
      b8=np.concatenate((b8,[frame[i,j]]),axis=0)
    for i in range(243,287):
     for j in range(243,287):
      b9=np.concatenate((b9,[frame[i,j]]),axis=0)
   if countf>10 and countf<15:
    b1[0]=b1[1]
    b2[0]=b2[1]
    b3[0]=b3[1]
    b4[0]=b4[1]
    b5[0]=b5[1]
    b6[0]=b6[1]
    b7[0]=b7[1]
    b8[0]=b8[1]
    b9[0]=b9[1]
    fravg1=np.concatenate((fravg1,[np.mean(b1,axis=0)]),axis=0)
    fravg2=np.concatenate((fravg2,[np.mean(b2,axis=0)]),axis=0)
    fravg3=np.concatenate((fravg3,[np.mean(b3,axis=0)]),axis=0)
    fravg4=np.concatenate((fravg4,[np.mean(b4,axis=0)]),axis=0)
    fravg5=np.concatenate((fravg5,[np.mean(b5,axis=0)]),axis=0)
    fravg6=np.concatenate((fravg6,[np.mean(b6,axis=0)]),axis=0)
    fravg7=np.concatenate((fravg7,[np.mean(b7,axis=0)]),axis=0)
    fravg8=np.concatenate((fravg8,[np.mean(b8,axis=0)]),axis=0)
    fravg9=np.concatenate((fravg9,[np.mean(b9,axis=0)]),axis=0)
   if countf==15:
       print(fravg1)
       fravg1[0]=fravg1[1]
       fravg2[0]=fravg2[1]
       fravg3[0]=fravg3[1]
       fravg4[0]=fravg4[1]
       fravg5[0]=fravg5[1]
       fravg6[0]=fravg6[1]
       fravg7[0]=fravg7[1]
       fravg8[0]=fravg8[1]
       fravg9[0]=fravg9[1]
       frav1= np.mean(fravg1,0)
       frav2= np.mean(fravg2,0)
       frav3= np.mean(fravg3,0)
       frav4= np.mean(fravg4,0)
       frav5= np.mean(fravg5,0)
       frav6= np.mean(fravg6,0)
       frav7= np.mean(fravg7,0)
       frav8= np.mean(fravg8,0)
       frav9= np.mean(fravg9,0)
   cv2.imshow('frame', frame1)
   cv2.imshow('red', result1)
   cv2.imshow('white', result2)
   cv2.imshow('yellow', result3)
   cv2.imshow('blue', result4)
   cv2.imshow('green', result5)
   cv2.imshow('orange', result6)
   if countf==15:
    if frav1[0]>91 and frav1[0]<114 and frav1[1]>130 and frav1[2]>133:
       print("1.blue")
    if frav2[0]>91 and frav2[0]<114 and frav2[1]>130 and frav2[2]>133:
       print("2.blue")
    if frav3[0]>91 and frav3[0]<114 and frav3[1]>130 and frav3[2]>133:
       print("3.blue")
    if frav4[0]>91 and frav4[0]<114 and frav4[1]>130 and frav4[2]>133:
       print("4.blue")
    if frav5[0]>91 and frav5[0]<114 and frav5[1]>130 and frav5[2]>133:
       print("5.blue")
    if frav6[0]>91 and frav6[0]<114 and frav6[1]>130 and frav6[2]>133:
       print("6.blue")
    if frav7[0]>91 and frav7[0]<114 and frav7[1]>130 and frav7[2]>133:
       print("7.blue")
    if frav8[0]>91 and frav8[0]<114 and frav8[1]>130 and frav8[2]>133:
       print("8.blue")
    if frav9[0]>91 and frav9[0]<114 and frav9[1]>130 and frav9[2]>133:
       print("9.blue")



    if frav1[0]>110 and frav1[0]<179 and frav1[1]>130 and frav1[1]<255 and frav1[2]>112 and frav1[2]<255:
       print("1.red")
    if frav2[0]>110 and frav2[0]<179 and frav2[1]>130 and frav2[1]<255 and frav2[2]>112 and frav2[2]<255:
       print("2.red")
    if frav3[0]>110 and frav3[0]<179 and frav3[1]>130 and frav3[1]<255 and  frav3[2]>112 and frav3[2]<255:
       print("3.red")
    if frav4[0]>110 and frav4[0]<179 and frav4[1]>130 and frav4[1]<255 and frav4[2]>112 and frav4[2]<255:
       print("4.red")
    if frav5[0]>110 and frav5[0]<179 and frav5[1]>130 and frav5[1]<255 and frav5[2]>112 and frav5[2]<255:
       print("5.red")
    if frav6[0]>110 and frav6[0]<179 and frav6[1]>130 and frav6[1]<255 and frav6[2]>112 and frav6[2]<255:
       print("6.red")
    if frav7[0]>110 and frav7[0]<179 and frav7[1]>130 and frav7[1]<255 and frav7[2]>112 and frav7[2]<255:
       print("7.red")
    if frav8[0]>110 and frav8[0]<179 and frav8[1]>130 and frav8[1]<255 and frav8[2]>112 and frav8[2]<255:
       print("8.red")
    if frav9[0]>110 and frav9[0]<179 and frav9[1]>130 and frav9[1]<255 and frav9[2]>112 and frav9[2]<255:
       print("9.red")
       
    if frav1[0]>20 and frav1[0]<64 and frav1[1]>60 and frav1[1]<227 and frav1[2]>127 and frav1[2]<200:
       print("1.green")
    if frav2[0]>20 and frav2[0]<64 and frav2[1]>60 and frav2[1]<227 and frav2[2]>127 and frav2[2]<200:
       print("2.green")
    if frav3[0]>20 and frav3[0]<64 and frav3[1]>60 and frav3[1]<227 and frav3[2]>127 and frav3[2]<200:
       print("3.green")
    if frav4[0]>20 and frav4[0]<64 and frav4[1]>60 and frav4[1]<227 and frav4[2]>127 and frav4[2]<200:
       print("4.green")
    if frav5[0]>20 and frav5[0]<64 and frav5[1]>60 and frav5[1]<227 and frav5[2]>127 and frav5[2]<200:
       print("5.green")
    if frav6[0]>20 and frav6[0]<64 and frav6[1]>60 and frav6[1]<227 and frav6[2]>127 and frav6[2]<200:
       print("6.green")
    if frav7[0]>20 and frav7[0]<64 and frav7[1]>60 and frav7[1]<227 and frav7[2]>127 and frav7[2]<200:
       print("7.green")
    if frav8[0]>20 and frav8[0]<64 and frav8[1]>60 and frav8[1]<227 and frav8[2]>127 and frav8[2]<200:
       print("8.green")
    if frav9[0]>20 and frav9[0]<64 and frav9[1]>60 and frav9[1]<227 and frav9[2]>127 and frav9[2]<200:
       print("9.green")

    if frav1[0]>20 and frav1[0]<64 and frav1[1]>61 and frav1[1]<255 and frav1[2]>153 and frav1[2]<255:
       print("1.yellow")
    if frav2[0]>20 and frav2[0]<46 and frav2[1]>61 and frav2[1]<255 and frav2[2]>153 and frav2[2]<255:
       print("2.yellow")
    if frav3[0]>20 and frav3[0]<46 and frav3[1]>61 and frav3[1]<255 and  frav3[2]>153 and frav3[2]<255:
       print("3.yellow")
    if frav4[0]>20 and frav4[0]<46 and frav4[1]>61 and frav4[1]<255 and frav4[2]>153 and frav4[2]<255:
       print("4.yellow")
    if frav5[0]>20 and frav5[0]<46 and frav5[1]>61 and frav5[1]<255 and frav5[2]>153 and frav5[2]<255:
       print("5.yellow")
    if frav6[0]>20 and frav6[0]<46 and frav6[1]>61 and frav6[1]<255 and frav6[2]>153 and frav6[2]<255:
       print("6.yellow")
    if frav7[0]>20 and frav7[0]<46 and frav7[1]>61 and frav7[1]<255 and frav7[2]>153 and frav7[2]<255:
       print("7.yellow")
    if frav8[0]>20 and frav8[0]<46 and frav8[1]>61 and frav8[1]<255 and frav8[2]>153 and frav8[2]<255:
       print("8.yellow")
    if frav9[0]>20 and frav9[0]<46 and frav9[1]>61 and frav9[1]<255 and frav9[2]>153 and frav9[2]<255:
       print("9.yellow")

    if frav1[0]>0 and frav1[0]<18 and frav1[1]>115 and frav1[1]<240 and frav1[2]>163 and frav1[2]<255:
       print("1.orange")
    if frav2[0]>0 and frav2[0]<18 and frav2[1]>115 and frav2[1]<255 and frav2[2]>163 and frav2[2]<255:
       print("2.orange")
    if frav3[0]>0 and frav3[0]<18 and frav3[1]>115 and frav3[1]<255 and  frav3[2]>163 and frav3[2]<255:
       print("3.orange")
    if frav4[0]>0 and frav4[0]<18 and frav4[1]>115 and frav4[1]<255 and frav4[2]>163 and frav4[2]<255:
       print("4.orange")
    if frav5[0]>0 and frav5[0]<18 and frav5[1]>115 and frav5[1]<255 and frav5[2]>163 and frav5[2]<255:
       print("5.orange")
    if frav6[0]>0 and frav6[0]<18 and frav6[1]>115 and frav6[1]<255 and frav6[2]>163 and frav6[2]<255:
       print("6.orange")
    if frav7[0]>0 and frav7[0]<18 and frav7[1]>115 and frav7[1]<255 and frav7[2]>163 and frav7[2]<255:
       print("7.orange")
    if frav8[0]>0 and frav8[0]<18 and frav8[1]>115 and frav8[1]<255 and frav8[2]>163 and frav8[2]<255:
       print("8.orange")
    if frav9[0]>0 and frav9[0]<18 and frav9[1]>115 and frav9[1]<255 and frav9[2]>163 and frav9[2]<255:
       print("9.orange")

    if frav1[0]>0 and frav1[0]<117 and frav1[1]>10 and frav1[1]<97 and frav1[2]>153 and frav1[2]<241:
       print("1.white")
    if frav2[0]>0 and frav2[0]<117 and frav2[1]>10 and frav2[1]<97 and frav2[2]>153 and frav2[2]<241:
       print("2.white")
    if frav3[0]>0 and frav3[0]<117 and frav3[1]>10 and frav3[1]<97 and  frav3[2]>153 and frav3[2]<241:
       print("3.white")
    if frav4[0]>0 and frav4[0]<117 and frav4[1]>10 and frav4[1]<97 and frav4[2]>153 and frav4[2]<241:
       print("4.white")
    if frav5[0]>0 and frav5[0]<117 and frav5[1]>10 and frav5[1]<97 and frav5[2]>153 and frav5[2]<241:
       print("5.white")
    if frav6[0]>0 and frav6[0]<117 and frav6[1]>10 and frav6[1]<97 and frav6[2]>153 and frav6[2]<241:
       print("6.white")
    if frav7[0]>0 and frav7[0]<117 and frav7[1]>10 and frav7[1]<97 and frav7[2]>153 and frav7[2]<241:
       print("7.white")
    if frav8[0]>0 and frav8[0]<117 and frav8[1]>10 and frav8[1]<97 and frav8[2]>153 and frav8[2]<241:
       print("8.white")
    if frav9[0]>0 and frav9[0]<117 and frav9[1]>10 and frav9[1]<97 and frav9[2]>153 and frav9[2]<241:
       print("9.white")

   key=cv2.waitKey(1)
   if countf == 100:
    break

cap.release()
cv2.destroyAllWindows()


#
#Usage, Just run the trajectory.py with the point and momentum atached after the command.
#Example: python trayectory.py x0 y0 z0 px py pz 
#
import sys
import math


#Set world size in mm inside the float parentheses

xWorld= float(230.00)*100/2
yWorld= float(230.00)*100/2
zWorld= float(230.00)*100/2


#Start Point
x0= float(sys.argv[1])*100
y0= float(sys.argv[2])*100
z0= float(sys.argv[3])*100


#Momentum
px= float(sys.argv[4])
py= float(sys.argv[5])
pz= float(sys.argv[6])


#Actual Volume Definition

def getVolume(x, y, z):

#Set Boundaries
  if(x < -xWorld or y < -yWorld or z < -zWorld or x > xWorld or y > yWorld or z > zWorld):
    return "Exit"

#Define lenght of arm
  
  if( z > 105.00 *100 or z < -105.00 *100 ):
    return "Air"
  
#Define Bone in mm before de *100 multiplier
  rb= 30.00 *100    #Bone radius
  xbc= 0 *100  #X cylinder center
  ybc= 0 *100  #Y cylinder center
#Ask for Bone
  if( pow( x-xbc ,2) + pow( y-ybc ,2) <= pow( rb ,2) ):
    return "Bone"

#Define Muscle in mm before de *100 multiplier
  rm= 100.00 *100   #Muscle radius
  xmc= 0 *100  #X muscle center
  ymc= 0 *100  #Y muscle center
#Ask for Muscle
  if( pow( x-xmc ,2) + pow( y-ymc ,2) <= pow( rm ,2) ):
    return "Muscle"

#Define Fat in mm before de *100 multiplier
  rf= 105.00 *100   #Fat radius
  xfc= 0 *100  #X fat center
  yfc= 0 *100  #Y fat center
#Ask for Fat
  if( pow( x-xfc ,2) + pow( y-yfc ,2) <= pow( rf ,2) ):
    return "Fat"

#Define Skin in mm before de *100 multiplier
  rs= 110.00 *100   #Skin radius
  xsc= 0 *100  #X skin center
  ysc= 0 *100  #Y skin center
#Ask for Skin
  if( pow( x-xsc ,2) + pow( y-ysc ,2) <= pow( rs ,2) ):
    return "Skin"

#Anything else is Air
  return "Air"


#Define trajectory

norm= math.sqrt( pow(px, 2) + pow(py, 2) + pow(pz, 2))
xt= px/norm
yt= py/norm
zt= pz/norm


#Set Initial Volume and Positions

xa= x0
ya= y0
za= z0
xb= x0
yb= y0
zb= z0
volume= getVolume(xa, ya, za)

#Set Distance and Points

i= 0
dis= [0,0,0,0,0,0,0,0,0]
pto= [[x0,y0,z0],
     [0,0,0],
     [0,0,0],
     [0,0,0],
     [0,0,0],
     [0,0,0],
     [0,0,0],
     [0,0,0],
     [0,0,0],
     [0,0,0]]


#Trayectory

if pow(xt, 2) >= pow(yt, 2) + pow(zt, 2):

  if xt <= 0: #X is desending
    stay= True
    while xb>-xWorld-1 and stay:
      
      xb= xb + xt
      yb= yb + yt
      zb= zb + zt
      
      if volume != getVolume(xb, yb, zb):    
        r= math.sqrt( pow(xb-xa ,2) + pow(yb-ya ,2) + pow(zb-za ,2))
        #print(round(r/100, 2), "\t mm in ", volume, " at:\t", round((xb-xt)/100, 2), round((yb-yt)/100, 2), round((zb-zt)/100, 2))
        
        dis[i]= r
        pto[i+1][0]= xb-xt 
        pto[i+1][1]= yb-yt
        pto[i+1][2]= zb-zt
        i= i+1
        
        xa= xb
        ya= yb
        za= zb
        volume= getVolume(xb, yb, zb)
        if volume == "Exit":
          stay= False
          #print(volume)
  
  
  else:  #X is asending
    stay=True
    while xb<xWorld+1 and stay:
      
      xb= xb + xt
      yb= yb + yt
      zb= zb + zt
      
      if volume != getVolume(xb, yb, zb):    
        r= math.sqrt( pow(xb-xa ,2) + pow(yb-ya ,2) + pow(zb-za ,2))
        #print(round(r/100, 2), "\t mm in ", volume, " at:\t", round((xb-xt)/100, 2), round((yb-yt)/100, 2), round((zb-zt)/100, 2))
        
        dis[i]= r
        pto[i+1][0]= xb-xt 
        pto[i+1][1]= yb-yt
        pto[i+1][2]= zb-zt
        i= i+1
        
        xa= xb
        ya= yb
        za= zb
        volume= getVolume(xb, yb, zb)
        if volume == "Exit":
          stay= False
          #print(volume)


elif pow(yt, 2) >= pow(xt, 2) + pow(zt, 2):

  if yt <= 0: #Y is desending
    stay= True
    while yb>-yWorld-1 and stay:
      
      xb= xb + xt
      yb= yb + yt
      zb= zb + zt
      
      if volume != getVolume(xb, yb, zb):    
        r= math.sqrt( pow(xb-xa ,2) + pow(yb-ya ,2) + pow(zb-za ,2))
        #print(round(r/100, 2), "\t mm in ", volume, " at:\t", round((xb-xt)/100, 2), round((yb-yt)/100, 2), round((zb-zt)/100, 2))
        
        dis[i]= r
        pto[i+1][0]= xb-xt 
        pto[i+1][1]= yb-yt
        pto[i+1][2]= zb-zt
        i= i+1
        
        xa= xb
        ya= yb
        za= zb
        volume= getVolume(xb, yb, zb)
        if volume == "Exit":
          stay= False
          #print(volume)
  
  
  else:  #Y is asending
    stay=True
    while yb<yWorld+1 and stay:
      
      xb= xb + xt
      yb= yb + yt
      zb= zb + zt
      
      if volume != getVolume(xb, yb, zb):    
        r= math.sqrt( pow(xb-xa ,2) + pow(yb-ya ,2) + pow(zb-za ,2))
        #print(round(r/100, 2), "\t mm in ", volume, " at:\t", round((xb-xt)/100, 2), round((yb-yt)/100, 2), round((zb-zt)/100, 2))
        
        dis[i]= r
        pto[i+1][0]= xb-xt 
        pto[i+1][1]= yb-yt
        pto[i+1][2]= zb-zt
        i= i+1
        
        xa= xb
        ya= yb
        za= zb
        volume= getVolume(xb, yb, zb)
        if volume == "Exit":
          stay= False
          #print(volume)
   
          
else:

  if zt <= 0: #Z is desending
    stay= True
    while zb>-zWorld-1 and stay:
      
      xb= xb + xt
      yb= yb + yt
      zb= zb + zt
      
      if volume != getVolume(xb, yb, zb):    
        r= math.sqrt( pow(xb-xa ,2) + pow(yb-ya ,2) + pow(zb-za ,2))
        #print(round(r/100, 2), "\t mm in ", volume, " at:\t", round((xb-xt)/100, 2), round((yb-yt)/100, 2), round((zb-zt)/100, 2))
        
        dis[i]= r
        pto[i+1][0]= xb-xt 
        pto[i+1][1]= yb-yt
        pto[i+1][2]= zb-zt
        i= i+1
        
        xa= xb
        ya= yb
        za= zb
        volume= getVolume(xb, yb, zb)
        if volume == "Exit":
          stay= False
          #print(volume)
  
  
  else:  #Z is asending
    stay=True
    while zb<zWorld+1 and stay:
      
      xb= xb + xt
      yb= yb + yt
      zb= zb + zt
      
      if volume != getVolume(xb, yb, zb):    
        r= math.sqrt( pow(xb-xa ,2) + pow(yb-ya ,2) + pow(zb-za ,2))
        #print(round(r/100, 2), "\t mm in ", volume, " at:\t", round((xb-xt)/100, 2), round((yb-yt)/100, 2), round((zb-zt)/100, 2))
        
        dis[i]= r
        pto[i+1][0]= xb-xt 
        pto[i+1][1]= yb-yt
        pto[i+1][2]= zb-zt
        i= i+1
        
        xa= xb
        ya= yb
        za= zb
        volume= getVolume(xb, yb, zb)
        if volume == "Exit":
          stay= False
          #print(volume)


#Set return Variabels

disf= [0,0,0,0,0,0,0]
ptof= [[0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0]]


#Arrange nubmer on return variables

m=-1
volume= getVolume(x0, y0, z0)

if volume == "Skin" and i > 5:
  m= 0

elif volume == "Fat" and i > 5:
  m= 1

elif volume == "Muscle" and i > 5:
  m= 2

elif volume == "Bone" :
  m= 3

elif volume == "Muscle" and i < 5:
  m= 4

elif volume == "Fat" and i < 5:
  m= 5

elif volume == "Skin" and i < 5:
  m= 6

for x in range(0,i-1,1):

  disf[x+m]= round((dis[x])/100, 2)
  
  ptof[x+m+1][0]= round((pto[x+1][0])/100, 2)
  ptof[x+m+1][1]= round((pto[x+1][1])/100, 2)
  ptof[x+m+1][2]= round((pto[x+1][2])/100, 2)


if volume == "Air":
  ptof[0][0]= round( pto[1][0]/100 ,2) 
  ptof[0][1]= round( pto[1][1]/100 ,2)
  ptof[0][2]= round( pto[1][2]/100 ,2)

else:

  ptof[m][0]= round( pto[0][0]/100 ,2) 
  ptof[m][1]= round( pto[0][1]/100 ,2)
  ptof[m][2]= round( pto[0][2]/100 ,2)


#Apply return

print(disf)
print(ptof)

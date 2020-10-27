#
#Usage, Just run the trajectory.py with the point and momentum atached after the command.
#Example: ./trayectory.py x0 y0 z0 px py pz 
#
import sys
import math


#Set world size in desired units in mm inside the float parentheses

xWorld= float(500.00)*100
yWorld= float(500.00)*100
zWorld= float(500.00)*100


#Start Point
x0= float(sys.argv[1])*100
y0= float(sys.argv[2])*100
z0= float(sys.argv[3])*100


#Momentum
px= float(sys.argv[4])*100
py= float(sys.argv[5])*100
pz= float(sys.argv[6])*100


#Actual Volume Definition

def getVolume(x, y, z):

#Set Boundaries
  if(x <0 or y <0 or z <0 or x >xWorld or y >yWorld or z >zWorld):
    return "Exit"
    
#Define Bone in mm before de *100 multiplier
  rb= 30.00 *100
  ybc= 250.00 *100
  zbc= 150.00 *100
#Ask for Bone
  if( pow( y-ybc ,2) + pow( z-zbc ,2) <= pow( rb ,2) ):
    return "Bone"

#Define Muscle in mm before de *100 multiplier
  rm= 100.00 *100
  ymc= 250.00 *100
  zmc= 150.00 *100
#Ask for Muscle
  if( pow( y-ymc ,2) + pow( z-zmc ,2) <= pow( rm ,2) ):
    return "Muscle"

#Define Fat in mm before de *100 multiplier
  rf= 105.00 *100
  pyc= 250.00 *100
  pzc= 150.00 *100
#Ask for Skin
  if( pow( y-pyc ,2) + pow( z-pzc ,2) <= pow( rf ,2) ):
    return "Fat"

#Define Skin in mm before de *100 multiplier
  rs= 110.00 *100
  ysc= 250.00 *100
  zsc= 150.00 *100
#Ask for Skin
  if( pow( y-ysc ,2) + pow( z-zsc ,2) <= pow( rs ,2) ):
    return "Skin"

#Anything else is Air
  return "Air"


#Define trajectory

norm= math.sqrt( pow(px, 2) + pow(py, 2) + pow(pz, 2))
xt= px/norm
yt= py/norm
zt= pz/norm


#Set Initial Volume and Positions

xa= x0+xt
ya= y0+yt
za= z0+zt
xb= x0
yb= y0
zb= z0
volume= getVolume(xa, ya, za)


#Trayectory

if pow(zt, 2) >= pow(xt, 2) + pow(yt, 2):

  if zt <= 0: #Z is desending
    stay= True
    while zb>-1 and stay:
      
      xb= xb + xt
      yb= yb + yt
      zb= zb + zt
      
      if volume != getVolume(xb, yb, zb):    
        r= math.sqrt( pow(xb-xa ,2) + pow(yb-ya ,2) + pow(zb-za ,2))
        print(round(r/100, 2), "\t mm in ", volume, " at:\t", round((xb-xt)/100, 2), round((yb-yt)/100, 2), round((zb-zt)/100, 2))
        xa= xb
        ya= yb
        za= zb
        volume= getVolume(xb, yb, zb)
        if volume == "Exit":
          stay= False
          print(volume)
  
  
  else:  #Z is asending
    stay=True
    while zb<zWorld+1 and stay:
      
      xb= xb + xt
      yb= yb + yt
      zb= zb + zt
      
      if volume != getVolume(xb, yb, zb):    
        r= math.sqrt( pow(xb-xa ,2) + pow(yb-ya ,2) + pow(zb-za ,2))
        print(round(r/100, 2), "\t mm in ", volume, " at:\t", round((xb-xt)/100, 2), round((yb-yt)/100, 2), round((zb-zt)/100, 2))
        xa= xb
        ya= yb
        za= zb
        volume= getVolume(xb, yb, zb)
        if volume == "Exit":
          stay= False
          print(volume)
        
elif pow(xt, 2) >= pow(yt, 2) + pow(zt, 2):

  if xt <= 0: #X is desending
    stay= True
    while xb>-1 and stay:
      
      xb= xb + xt
      yb= yb + yt
      zb= zb + zt
      
      if volume != getVolume(xb, yb, zb):    
        r= math.sqrt( pow(xb-xa ,2) + pow(yb-ya ,2) + pow(zb-za ,2))
        print(round(r/100, 2), "\t mm in ", volume, " at:\t", round((xb-xt)/100, 2), round((yb-yt)/100, 2), round((zb-zt)/100, 2))
        xa= xb
        ya= yb
        za= zb
        volume= getVolume(xb, yb, zb)
        if volume == "Exit":
          stay= False
          print(volume)
  
  
  else:  #X is asending
    stay=True
    while xb<zWorld+1 and stay:
      
      xb= xb + xt
      yb= yb + yt
      zb= zb + zt
      
      if volume != getVolume(xb, yb, zb):    
        r= math.sqrt( pow(xb-xa ,2) + pow(yb-ya ,2) + pow(zb-za ,2))
        print(round(r/100, 2), "\t mm in ", volume, " at:\t", round((xb-xt)/100, 2), round((yb-yt)/100, 2), round((zb-zt)/100, 2))
        xa= xb
        ya= yb
        za= zb
        volume= getVolume(xb, yb, zb)
        if volume == "Exit":
          stay= False
          print(volume)

else:

  if yt <= 0: #Y is desending
    stay= True
    while yb>-1 and stay:
      
      xb= xb + xt
      yb= yb + yt
      zb= zb + zt
      
      if volume != getVolume(xb, yb, zb):    
        r= math.sqrt( pow(xb-xa ,2) + pow(yb-ya ,2) + pow(zb-za ,2))
        print(round(r/100, 2), "\t mm in ", volume, " at:\t", round((xb-xt)/100, 2), round((yb-yt)/100, 2), round((zb-zt)/100, 2))
        xa= xb
        ya= yb
        za= zb
        volume= getVolume(xb, yb, zb)
        if volume == "Exit":
          stay= False
          print(volume)
  
  
  else:  #Y is asending
    stay=True
    while yb<zWorld+1 and stay:
      
      xb= xb + xt
      yb= yb + yt
      zb= zb + zt
      
      if volume != getVolume(xb, yb, zb):    
        r= math.sqrt( pow(xb-xa ,2) + pow(yb-ya ,2) + pow(zb-za ,2))
        print(round(r/100, 2), "\t mm in ", volume, " at:\t", round((xb-xt)/100, 2), round((yb-yt)/100, 2), round((zb-zt)/100, 2))
        xa= xb
        ya= yb
        za= zb
        volume= getVolume(xb, yb, zb)
        if volume == "Exit":
          stay= False
          print(volume)

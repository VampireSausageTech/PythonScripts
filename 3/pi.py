import math

"""
     /¦
 h  / ¦ o
   /x ¦ 
  -----
     a
h always equals 144 (radius of circle)

sin(x)=o/h
sin(x)=o/144    ¦ *144
sin(x)*144=o

cos(x)=a/h
cos(x)=a/144    ¦ *144
cos(x)*144=a
"""
def finddistance(p1,p2):
    return (math.sqrt( (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 ))
def findo(ang,h):
    return (math.sin(math.radians(ang))*h)
def finda(ang,h):
    return (math.cos(math.radians(ang))*h)
h=100

print(findo(45,100))
print(finda(45,100))

oldpoint=[finda(0.1,h),findo(0.1,h)]
ang=0.2
dis=0
while ang < 90.0000000000000000000000000000000000000000000000001:
    newpoint=[finda(ang,h),findo(ang,h)]
    dis+=finddistance(newpoint,oldpoint)
    oldpoint=newpoint
    ang+=0.000001
    print(ang/90*100)
    if ang%1.0 == 0.0:
        print(ang)
print(dis*4/(2*h))

while True:
    msg=input("")

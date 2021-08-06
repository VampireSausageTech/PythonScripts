import math
radius=100000000
#radius=100000
y=0
area1=0
area2=0
step=int(radius/20)
radiussq=radius**2
while y != radius:
    y+=1
    temp=math.sqrt(radiussq-y**2)
    area1+=math.floor(temp)
    area2+=math.ceil(temp)
    if y%step == 0:
        print(math.ceil(100*y/radius))
print("Minimum Value of Pi:")
pimin=4*area1/(radiussq)
print(pimin)
print("Maximum Value of Pi:")
pimax=4*area2/(radiussq)
print(pimax)
print("Averaged Value of Pi:")
print((pimin+pimax)/2)

"""
Imagine a quarter of a cirlce on a grid
At any given y value, we can find the x value if we know the radius using pythagrous. (x^2+y^2=r^2 -> x^2=r^2-y^2)
Therefore if we round x down, we know that there is rounded down x full units of area in that row.
If we repeat that for all values of y and add all of those rounded down x values together, we know that the area is at least that.
Then we get area of a circle formula and manipulate it (A=pi*r^2 -> pi=A/(r^2))
Then we have a minimum value of pi.

I have also logged maximum area in this one to calculate maximum pi.
I then average the pi to get a coler guess.
"""

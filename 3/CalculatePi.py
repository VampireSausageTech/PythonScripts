import math
radius=10000000
#radius=100
y=0
area=0
step=int(radius/20)
radiussq=radius**2
while y != radius:
    y+=1
    area+=math.floor(math.sqrt(radiussq-y**2))
    if y%step == 0:
        print(math.ceil(100*y/radius))
print(area)
print(4*area/(radiussq))


"""
Imagine a quarter of a cirlce on a grid
At any given y value, we can find the x value if we know the radius using pythagrous. (x^2+y^2=r^2 -> x^2=r^2-y^2)
Therefore if we round x down, we know that there is rounded down x full units of area in that row.
If we repeat that for all values of y and add all of those rounded down x values together, we know that the area is at least that.
Then we get area of a circle formula and manipulate it (A=pi*r^2 -> pi=A/(r^2))
Then we have a minimum value of pi.
"""

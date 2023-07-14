from math import sin
import math
# --example--
# print(sin(0))
# >>> 0
# -----------
k=0
a=0
b=math.pi/2
h=(b-a)/100
area = sum((h/2)*((sin(a+(k-1)*h))+sin(a+(k*h)))  for k in range(1,101))
print(area)

from math import sin
import math
# --example--
# print(sin(0))
# >>> 0
# -----------

def trapezoidal_integral(a,b,n,f):
    h=(b-a)/n
    area = sum((f(a+(k-1)*h)+f(a+k*h))*h/2  for k in range(1,n+1))
    return area
# def sin(x):
#     return math.sin(x)
trapezoidal_integral(0,math.pi/2,50,math.sin)
def func1(x):
    return 4/(1+x*x)
trapezoidal_integral(0,1,100,func1)
def func2(x):
    return math.pi**(1/2)*math.e**(-x**(2))
trapezoidal_integral(-100,100,1000,func2)

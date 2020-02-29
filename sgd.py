import numpy as np
#to minimise f=x**2+y**2+z**2 using sgd
x=np.random.randn(3,1)
print("inital value of x,y,z are ")
print(x)
for i in range (0,100):
    a=np.random.randn(3,1)
    df=2*a
    delx=0.9*df
    x=x-delx
print("optimised value of x,y,z are ")
print(x)

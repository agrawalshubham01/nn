import numpy as np
#to minimise f=x**2+y**2+z**2
a=np.random.randn(3,1)
print("inital value of x,y,z are ")
print(a)
df=1
#a is input
#df is partial differentiation array
for i in range (0,1000):
    da=0.9*df
    a=a-da
    df=2*a
print("optimised value of x,y,z are ")
print(a)

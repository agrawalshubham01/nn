import numpy as np
#to minimise f=x**2+y**2+z**2
a=np.random.rand(3,1)
a=np.float64(a)
print("inital value of x,y,z are ")
print(a)
#a is all variables
sumdelx2=0
sumdelx2=np.float64(sumdelx2)
#sumdelx2 is for rms of delta x
#df is partial differentiation array
# df2 is partial differentiation square
k=np.zeros((3,1))
# k is running sum of df2
g=np.random.rand(3,1)
df=2*g
df2=df**2
k=0.9*k+0.1*df2
c=(0.9)
b=(k+0.00001)**1/2
b=np.float64(b)
da=np.dot((c/b).T,df)
da=np.float64(da)
sumdelx2=0.9*sumdelx2 + 0.1*np.square(da)
a=a-da
for i in range (0,1):
    g=np.random.rand(3,1)
    df=2*g
    df2=df**2
    k=0.9*k+0.1*df2
    c=(sumdelx2+0.00001)**1/2
    b=(k+0.00001)**1/2
    da=np.dot((c/b).T,df)
    a=a-da
    sumdelx2=0.9*sumdelx2 + 0.1*np.square(da)
a = a.astype('float64')
print("optimised value of x,y,z are ")
print(a)

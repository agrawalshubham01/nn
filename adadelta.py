import numpy as np
#to minimise f=x**2+y**2+z**2
a=np.random.rand(3,1)
print("inital value of x,y,z are ")
print(a)
#a is all variables
#n, m, q are for randomizing the functions
sumdelx2=0
#sumdelx2 is for rms of delta x
#df is partial differentiation array
# df2 is partial differentiation square
k=np.zeros((3,1))
# k is running sum of df2
l=np.zeros((3,1))
# l is running sum of
n=np.random.normal()
m=np.random.normal()
q=np.random.normal()
df=np.array([[2*n],[2*m],[2*q]])
df2=np.array([[4*n**2],[4*m**2],[4*q**2]])
k=0.9*k+0.1*df2
c=(0.9)
b=(k+0.00001)**1/2
da=np.dot((c/b).T,df)
sumdelx2=0.9*sumdelx2 + 0.1*da**2
a=a-da
for i in range (0,999):
    n=np.random.normal()
    m=np.random.normal()
    q=np.random.normal()
    df=np.array([[2*n],[2*m],[2*q]])
    df2=np.array([[4*n**2],[4*m**2],[4*q**2]])
    k=0.9*k+0.1*df2
    c=(sumdelx2+0.00001)**1/2
    b=(k+0.00001)**1/2
    da=np.dot((c/b).T,df)
    a=a-da
    sumdelx2=0.9*sumdelx2 + 0.1*da**2
print("optimised value of x,y,z are ")
print(a)

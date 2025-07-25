import numpy as np
from numpy import *

def coeficients(x,y) :
    ''' x: absisas x_i 
        y : ordenadas f(x_i)'''
    n = len(x)
    F = zeros((n,n), dtype=float)
    b = zeros(n) 
    for i in range(0,n):
        F[i,0]=y[i]



    for j in range(1, n):
        for i in range(j,n):
            F[i,j] = float(F[i,j-1]-F[i-1,j-1])/float(x[i]-x[i-j])


    for i in range(0,n):
        b[i] = F[i,i]

    return np.array(b) 

def Eval(a, x, r):

    '''  a : retorno de la funcion coeficiente() 
         x : abcisas x_i
         r : abcisa a interpolar
    '''

    x.astype(float)
    n = len( a ) - 1
    temp = a[n]
    for i in range( n - 1, -1, -1 ):
        temp = temp * ( r - x[i] ) + a[i]
    return temp 

x = []
y= []
number = int(input("Enter number of values: "))
for _ in range(number):
    x_value = float(input("Enter X value: "))
    y_value =  float(input("Ente  Y value: "))

    x.append(x_value)
    y.append(y_value)

coef = coeficients(x,y)

for value in coef:
    print(value)
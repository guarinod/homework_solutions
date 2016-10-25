# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def karatsuba(x,y):
    #print('karatsuba start')
    X=str(x)
    Y=str(y)
    
    if ((len(X) == 1) | (len(Y) == 1)):
        #print('karatsuba end with '+str(x*y))        
        return x*y
    if (len(X) > len(Y)):
        if (len(X)%2 == 1):
            X = '0'+X
            Y = '0'*(len(X)-len(Y)) + Y
        else:
            Y = '0'*(len(X)-len(Y)) + Y
    elif (len(Y) > len(X)):
        if (len(Y)%2 == 1):
            Y = '0' + Y
            X = '0'*(len(Y)-len(X)) + X
        else:
            X = '0'*(len(Y)-len(X)) + X
    elif (len(X)%2 == 1) & (len(Y)%2 == 1):
        Y = '0' + Y
        X = '0' + X
        
    a=X[0:int((len(X))/2)]; #print(a)
    b=X[int((len(X))/2):]; #print(b)
    c=Y[0:int((len(Y))/2)];    #print(c)
    d=Y[int((len(Y))/2):];    #print(d)
    n = int(len(X));    #print('calculating ac')
    ac= karatsuba(int(a),int(c));    #print('calculating bd')    
    bd = karatsuba(int(b),int(d));    #print('calculating adpbc')    
    adpbc = karatsuba(int(a)+int(b),int(c)+int(d)) - ac - bd;    #print('karatsuba end with '+str(( int(str(ac) + '0'*n) + int(str(adpbc) + '0'*int(n/2)) + bd )))
    return ( int(str(ac) + '0'*n) + int(str(adpbc) + '0'*int(n/2)) + bd ) 
    
    
    
    
    
    
    
    
    
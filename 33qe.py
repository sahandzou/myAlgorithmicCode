# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:37:07 2016

@author: sahand
"""
import math as m
def test():
    for p in range(2,50):
        if ls[ln-x-p]!=0 :
            return 0
    return 1
ls=[]
ln=500
for x in range(ln):
    ls.append(0)
ls[ln-1]=1
y=2
x=1
h=365
for f in range(h):
    x=1
    j=0
    r1=0
    while(1):
        if(x==1):
            
            ls[ln-x]*=y
            ls[ln-x-1]*=y
            r=ls[ln-x]%10
            ls[ln-x-1]+=((ls[ln-x]-r)/10)
            j=ls[ln-x-1]%10
            r1=((ls[ln-x-1]-j)/10)
            ls[ln-x]=r
            ls[ln-x-1]=j

                        
            if(r1==0 and ( test())):
                break
            x+=1
            
        else:
            
            ls[ln-x]*=y
            ls[ln-x]+=r1
            r=ls[ln-x]%10
            r1=((ls[ln-x]-r)/10)
            print(r)
            ls[ln-x]=r
            print(r1)
            if(r1==0 and ( test())):
                break
        x+=1
    
        
    y+=1
print(ls)
print(m.factorial(h+1))
    
    
    
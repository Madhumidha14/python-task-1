# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:11:37 2021

@author: DELL
"""

def triangle(n):
    k = n-1 #number of spaces
    for i in range(0, n):# handles no of rows
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("*", end=" " )
        print("\r")
n=5
triangle(n)
            
        
        
        
        
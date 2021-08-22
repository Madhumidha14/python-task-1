# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:26:38 2021

@author: DELL
"""

Terms = int(input("enter the number of fibonacci terms:"))
A = 0
B = 1
sum = 0
if Terms<=0:
    print("enter the valid number of terms")
else:
     for i in range(0,Terms):
         print(sum,end=(" "))
         A = B
         B = sum
         sum = A + B
            
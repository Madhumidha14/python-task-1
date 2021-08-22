# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:42:38 2021

@author: DELL
"""

myList1 = [12,-7,5,64,-14]
print("numbers in the myList1 are:",myList1)
positive_num1 = list(filter(lambda x: x >0, myList1))
print ("the positive numbers are:", positive_num1)
myList2 = [12,14,-95,3]
print("numbers in the myList2 are:",myList1)
positive_num2 = list(filter(lambda x: x >0, myList2))
print ("the positive numbers are:", positive_num2)
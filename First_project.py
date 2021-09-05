# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 10:29:36 2021

@author: DELL
"""
import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a' , newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
         writer.writerow(["Name", "Age","Contact number","Mail id"])
        writer.writerow(info_list)
if __name__ == '__main__':
    condition = True
    student_number = 1
    while(condition):
        
        student_info = input("Enter the #{} student's information(Name,age,contact number,mail id):".format(student_number))
                
        student_list = student_info.split(' ')
        print("\nthe entered information is-\nName:{} \nAge:{} \nContact number:{} \nMail id:{}".format(student_list[0],student_list[1],student_list[2],student_list[3]))
       
        choice = input("is the entered information is correct?(yes/no):")
        if choice == "yes":
                 write_into_csv(student_list)
            
                 check = input("if you want to enter another type (yes/no):" )
                 if check == "yes":
                        condition = True
                        student_number += 1
                        
                 else:
                        condition = False
        elif choice == "no":
            print("\n please re-enter the values!")
                 
            

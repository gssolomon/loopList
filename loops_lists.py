# -*- coding: utf-8 -*-

#Created on Tue Dec  5 15:37:50 2017

#@author: glenn


#User inserts any value between 1 to 1,000,001
num=int(input("Enther the positive number:"))

#Prints user input value
print("User Entered:", num)

#Counter is for counting the number of iterations.
counter = 0

#num_list is for storing the intermediate values.
num_list = []

#What if the user entered value 1?
if(num==1):
    print("User entered value 1. So no iterations!")
    num_list.append(num)
    
#--------THE LOOP-----------
while (num!=1):    
    if(num%2==0):    #Checks is even or not
        num=num/2
        num_list.append(num)
        #print(num)
    else:            #If num is odd
        num=(num*3)+1
        num_list.append(num)
        #print(num)
        
    counter+=1
    
print("Number of iterations:", counter)
print("Intermediate values:", num_list)
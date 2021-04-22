#!/usr/bin/python 

a =int(input()) #get input from user

if (a%4==0 and a%100!=0 or a%400==0): #formula for find leap year
    print("YES")
else:
    print("NO")


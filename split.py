#!/usr/bin/python

a=input() #get input from user  eg; 123

b=list(a) #change to list format now its look like eg; ['1' '2' '3']

ans=' '.join(map(str, b)) #to change list format to string format

print(ans)



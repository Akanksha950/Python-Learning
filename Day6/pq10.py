# 11.Write a program that prints the multiplication table of any number entered by
# the user using a for loop.

num=int(input("Enter any number:"))
for i in range(1,11,1):
    print(num,"*",i,"=",num*i)
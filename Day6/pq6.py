# 7.Write a program to print the multiplication table of any number using a while
# loop.

num=int(input("Enter a number:"))
i=1
while(i<=10):
    print(num,"*",i,"=",num*i)
    i=i+1
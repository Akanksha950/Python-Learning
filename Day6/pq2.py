# 3.Write a program to print all even numbers between 1 and 50 using a while loop.

even=2
while(even<=50):
    print(even)
    even=even+2

print("All even nos from 1 to 50")

# or

even=1
while(even<=50):
    if(even%2==0):
        print(even)
    even=even+1

print("All even nos from 1 to 50")
# 5. Write a program to print this pattern using a while loop:
# *
# * *
# * * *
# * * * *

j=1
while(j<=4):
    print(j * "*")
    j=j+1

# using for loop

for i in range(1,4):
    for j in range(i):
        print("*", end="")
    print()

# 14.Print numbers from 1 to 100 using a for loop.

for i in range(1,101):
    print(i)

# 15.Print numbers from 100 to 1 using a while loop.

num=100
while(num>=1):
    print(num)
    num=num-1

# 16.Print all numbers between 1 and 50 except multiples of 5.

for i in range(1,51):
    if(i%5!=0):
        print(i)

# 17.Create a program that asks the user for 5 favorite foods and prints them one
# by one.

for i in range(5):
    food=input("Enter your favorite food:")
    print(food)


# 18.Print the sum of first 10 natural numbers using a while loop.

count=0
num=1
while(num<=10):
    count=count+num
    num=num+1
    
print(count)

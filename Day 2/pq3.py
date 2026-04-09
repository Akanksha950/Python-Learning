# Write a program that takes two numbers and prints:
# Their sum, difference, and product
# Whether the first number is greater than the second


a=int(input("enter first value:"))
b=int(input("enter second value:"))
sum=a+b
difference=a-b
product=a*b
print("sum of two numbers is:", sum)
print("difference of two numbers is:", difference)
print("product of two numbers is :", product)

if(a>b):
    print("First number is greater than second number")
elif(a<b):
    print("Second number is greater than first number")
else:
    print("Both numbers are equal")
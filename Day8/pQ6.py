# 5.Write a function greet_user(name) that prints a personalized message for Saumya Singh.

def greet_user(name):
    print(f"Hello, {name}! Welcome!")

greet_user("Saumya singh")

# 7.Write a function to return the largest of 3 numbers.

def largest(num1=5,num2=10,num3=15):
    if(num1>num2) and (num1>num3):
        print(f"{num1} is greater ")
    elif(num2>num3):
       print(f"{num2} is greater")
    else:
        print(f"{num3} is greater")
    
largest(10,150,30)
largest()
      
# 9.Write a function that returns both the sum and average of 5 inputs.

def avSum(num1,num2,num3,num4,num5):
    sum=num1+num2+num3+num4+num5
    avg=num1+num2+num3+num4+num5/5
    return sum,avg

result=avSum(1,2,3,4,5)
print("Sum:",result[0],"Average:",result[1])

# 10.Write a program to count vowels in a string using a function.

def count(input):
    vowel="aeiouAEIOU"
    v_count=0
    for i in input:
        if i.isalpha():
            if i in vowel:
                v_count=v_count+1
    
    return v_count
    
res=count("Hello Everyone")
print("Vowel=",res)

# 1.Write a function to calculate the factorial of a number.

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

print(fact(5))
# 1.Write a recursive function that prints numbers from 1 to N.

def num(n):
    if n==0:
        return
    num(n-1)
    print(n)
    
num(5)
       
# 2. sum of natural numbers from 1 to n

def sum(n):
    if n==0:
      return 0 
    else:
        return n+ sum(n-1)
    
print(sum(5))


# 3.Write a recursive function to calculate the factorial of a number.

def fact(n):
    if n==0:
        return 1
    else:
       return n*fact(n-1)
    
n=int(input("enter any number:"))
print("Factorial is=",fact(n))


# iterative function

def facto(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
    
print(facto(5))


# 4. Write a recursive function to print the Fibonacci series up to N terms.

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(5))


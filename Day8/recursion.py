# Factorial

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
print(factorial(0))
print(factorial(1))

# Fibonacci

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
Result=fibonacci(6)
print("fibonacci=",Result)
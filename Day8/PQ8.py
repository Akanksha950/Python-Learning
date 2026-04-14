# 2.Write a recursive function to print numbers from 1 to N.

def num(n):
    if n==0:
        return
    num(n-1)
    print(n)
num(5)

# 3.Write a function that checks if a number is prime.

def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i==0:
          return False
    return True

print(prime(5))

# 4.Write a recursive function to find the sum of first N natural numbers.

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
        
print(sum(5))

# 6.Write a recursive program to print the reverse of a string.
def reverse(n):
    if n=="":
        return 
    reverse(n[1:])
    print(n[0],end="")

reverse("\n python")


# 8.Write a recursive function to print even numbers from 2 to N.

def even(n):
    if n<2:
        return 
    even(n-2)
    print(n)
even(10)

# or

def even1(n):
    if n<2:
        return 
    even1(n-1)
    if n % 2 == 0:
        print(n)

even1(10)


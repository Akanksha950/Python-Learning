# 1. Write a program that takes a sentence and prints:
# ● Total characters (len())
# ● Uppercase version
# ● Lowercase version

str=input("Enter sentence:")
print("Total characters:",len(str))
print("Uppercase:",str.upper())
print("Lowercase:",str.lower())

# 2. Write a Python program that takes any word or sentence as input and prints:
# ● The first character
# ● The last character
# ● The total number of characters

str1=input("Input:")
len=len(str1)
print("First character:",str1[0])
print("Last character:",str1[len-1])
print("Total characters:",len)


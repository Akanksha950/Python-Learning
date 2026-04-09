# Write a Python program that takes a user’s name as input and prints:
# 1. The first character
# 2. The last character
# 3. The total length of the name


food_name=input("Enter favorite food name:")
mid=len(food_name)//2
print(food_name[mid-1:mid+2])

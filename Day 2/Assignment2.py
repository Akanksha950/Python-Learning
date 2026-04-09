#Smart Temperature Converter
#Take input in Celsius and print its equivalent in Fahrenheit and Kelvin.

temp=int(input("enter temperature in celsius:"))
f=(temp*9/5)+32
k=temp+273.15
print("Fahrenheit:",f)
print("Kelvin:",k)

# Bill Split Calculator
# Write a program that takes total bill amount and number of friends as input.
# Calculate how much each person will pay.
# Also print the data type of each variable used.

total_bill=int(input("Total bill :"))
num_friends=int(input("Friends:"))
final_bill=total_bill/num_friends
print("Each will pay:",final_bill)
print("Data type of total_bill is  :", type(total_bill))
print("Data type of num_friends  is :",type(num_friends))
print("Data type of final_bill is :",type(final_bill))


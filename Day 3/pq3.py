# Write a program that:
# ● Takes a sentence as input
# ● Converts it to lowercase
# ● Replaces all spaces " " with underscores "_"
# ● Prints the new string

str=input("Enter any message:")
lower=str.lower()
new_str=lower.replace(" ","_")
print(new_str)
# medium questions
# 1. Create a file named saumya_info.txt using "x" mode.

file=open("saumya_info.txt","x")

# 2.Write a program to safely check whether a file exists before opening it.

try:
    with open("D:\PYTHON\Day10\demo.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File does not exist.")

x=12     # global variable
def show():
    x=5  # local variable
    print("Inside function=",x)
show()
print("outside function",x)
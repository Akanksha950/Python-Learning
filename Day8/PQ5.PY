# 1.Write a program with a local variable score inside a function and a global one outside.

score=30
def play():
    score=20
    print(score)
play()
print(score)

# 2. Create a program using global keyword to modify a variable from inside a function.

x=20
def update():
    global x
    x=4
    print("Updated value inside function",x)

update()
print("outside the function:",x)





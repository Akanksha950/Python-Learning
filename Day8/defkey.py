def std_info(name,age):
    print(name,"is",age,"years old.")

std_info(name="akanksha",age=21)

# 1.Define a function message(text="Keep Learning!") and call it with and without an argument.

def message(text="Keep Learning!"):
    return text
print((message("Let's Crack it")))
print(message())

# 2.Create a function login(username, password="1234") that prints the credentials.

def login(username,password="1234"):
    print("username=",username)
    print("password=",password)
login("akanksha")
login("soni","345")
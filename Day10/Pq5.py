# 1.Use with to read the entire content of info.txt.
with open("info.txt","r") as f:
    print(f.read())

# 2.Use with to write "Hello World" in hello.txt.
with open("hello.txt","w")as f:
    f.write("Hello World")
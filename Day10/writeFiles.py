# writing files 
with open("demo.txt","w") as f:
    f.write("This is my first python file.")

# append mode
with open("demo.txt","a") as f:
    f.write("More content added.")   
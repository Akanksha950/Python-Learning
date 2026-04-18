# read entire files
with open("notes.txt","r") as f:
    data=f.read()
    print(data)

# read line by line
with open("notes.txt","r") as f:
    line1=f.readline()
    line2=f.readline()
    line3=f.readline()
    line4=f.readline()
    data=f.read()
    print("line1:",line1)
    print("line2:",line2)
    print("line3:",line3)
    print("line4:",data)
    print("line4:",line4)

# read all lines
with open("notes.txt","r") as f:
    lines=f.readlines()
    print(lines)


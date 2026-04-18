# 1.Write code to open a file named mydata.txt in read mode.

f=open("mydata.txt","r")
print(f.read())

# 2.Write a program to read a text from a given file certificate.txt and find whether it contains the word live.

file=open("certificate.txt","r")
data=file.read()
print(data)

data=data.lower()
if "live" in data:
    print("yes live word is present in file")
else:
    print("no")


# 3.What happens if you open a non-existing file in "r" mode?

# -> it will give error that such file don't exit,file not found


# 4.Open a file called report.txt in write mode.

file=open("report.txt","w")
file.write("I am learning python")

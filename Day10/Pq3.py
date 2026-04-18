# 1.Read a file named story.txt and print the full content.

with open("story.txt","r") as f:
    data=f.read()
    print(data)

# 2.Read only the first line of bio.txt.

with open("bio.txt","r") as f:
    line1=f.readline()
    print(line1)

# 3.Print how many lines are present in notes.txt.

with open("notes.txt","r") as f:
    lines=f.readlines()
    print(len(lines))
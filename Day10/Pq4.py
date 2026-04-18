# 1.Write your name and class into a file named intro.txt.

with open("intro.txt","w")as f:
    f.write("My name is Akanksha Kumari and i am in 12 class.")

# 2.Create a file goals.txt and write 3 goals for this month.

with open("goals.txt","w")as f:
    f.write("My goals are:")
    f.write("\n 1.Eating Healthy")
    f.write("\n 2.complete python course")
    f.write("\n 3.Crack a good job")

# 3.Append "Completed" to an existing file status.txt.

with open("status.txt","a") as f:
    f.write("Completed")



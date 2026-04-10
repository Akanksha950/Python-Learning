#Ask the user for their 3 favorite movies and store them in a list.

movie1=input("Enter fav movie:")
movie2=input("Enter fav movie:")
movie3=input("Enter fav movie:")
movieList=[movie1,movie2,movie3]
print(movieList)

#Create a tuple of marks (87, 64, 33, 95, 76) and print the highest and lowest marks using max() and min().

marks=(87,64,33,95,76)
print(max(marks))
print(min(marks))

# Write a program to check grade based on marks (A/B/C/D) using if-elif-else.

marks=int(input("Enter marks:"))
if(marks>=90):
    print("Grade A")
elif(marks>=80):
    print("Grade B")
elif(marks>=70):
    print("Grade C")
else:
    print("Grade D")
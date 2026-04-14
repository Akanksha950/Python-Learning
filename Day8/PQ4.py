# 1. Write a function square(num) that returns the square of a number.

def square(num=6):
    return num*num

print(square(5))
print(square())

# 2.Write a function that takes a string and returns the count of vowels and consonants separately.

def countVowCons(userInput):
   vowels="aeiouAEIOU"
   v_count=0
   c_count=0

   for ch in userInput:
       if ch.isalpha():
            if ch in vowels:
               v_count=v_count+1
            else:
               c_count=c_count+1

   return v_count,c_count

v,c=countVowCons("Akanksha Kumari")
print("Vowels=",v,"Consonants=",c)

# 3.Define a function convert_to_upper(word) that returns the uppercase version of the string.

def convert_to_upper(word):
    return word.upper()

# input=convert_to_upper("i am learning python")
user_text=input("Enter a sentence:")
res=convert_to_upper(user_text)
print(res)

# 4.Create a function full_name(fname, lname) that returns the full name joined with a space.

def full_name(fname,lname):
    return(fname + " " + lname)

res=full_name("akanksha","kumari")
print(res)

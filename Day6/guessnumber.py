# Guess the Number Game


secret_number = 7  

name = input("Enter your name: ")

guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == secret_number:
        print("Congratulations,", name, "! You guessed it right 🎉")
    else:
        print("Wrong guess! Try again.")


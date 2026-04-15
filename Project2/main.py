# RULE BASED CHAT ASSISTANT
import datetime
import time

name=input("Enter your name:")
hour=datetime.datetime.now().hour

if 5<= hour <12:
    print("Good morning,name")
elif 12<= hour <17:
    print("Good afternoon",name)
elif 17 <= hour<21:
    print("Good evening",name)
else:
    print("Good night",name)


print("Namaste! I am your mini chatbot")
print("You can talk to me.Type 'bye' anytime to exit.\n")

# Add at least 3 new questions and responses to the chatbot.

response={
    "hello":"Hi,welcome.How can I help you?",
    "how are you":"I am very fine.Thank you",
    "who are you":"I am smart AI chatbot",
    "motivate me":"keep going. Every bug of your project make you a better developer",
    "happy":"Great to hear that"
}

#function to get response
def getResponse(userQuestion):
    userQuestion=userQuestion.lower()
    for key in response:
        if key in userQuestion:
            return response[key]
    
    return "I’m not sure about that yet, but I’ll learn soon!"

# take input from user
while True:
   user=input("Please ask your question:")
   reply=getResponse(user)
   print("Bot Response:",reply)

   if "bye" in user.lower():
       break
   




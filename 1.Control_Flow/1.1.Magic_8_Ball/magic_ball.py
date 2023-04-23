#Python program that can answer any “Yes” or “No” question with a different fortune each time it executes. 
#No interface, might be devloped later...

import random

#Declaration section
name = "Ricky"
question = "Will my next football season be better then my last?"
answer =""
random_number = random.randint(1, 9)


#Program logic - practicing concepts of conditional statements
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer ="Without a doubt"
elif random_number == 4:
  answer ="Reply hazy, try again"
elif random_number == 5:
  answer ="Ask again later"
elif random_number == 6:
  answer ="Better not tell you now"
elif random_number == 7:
  answer ="My sources say no"
elif random_number == 8:
  answer ="Outlook not so good"
elif random_number == 9:
  answer ="Very doubtful"
else:
  answer = "Error"

#Terminal outputs (running script in terminal)
#Conditional statements that also take in consideration if no name or question is typed
if name == "":
  if question !="":
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
  if question == "":
    print("You haven't enetered a name or question")
elif question == "":
  print("You must enter a question")
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)
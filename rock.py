import random

choices = ['rock','paper','scissor']

computer = random.choice(choices)
user = 'scissor'

print("User's choice: ",user)
print("Computer's choice: ",computer)

if (user=='rock' and computer=='scissor') or (user=='paper' and computer=='rock') or (user=='scissor' and computer=='paper'):
    print("User Won")
elif user==computer:
    print("Its a TIE")
else:
    print("Computer Won")
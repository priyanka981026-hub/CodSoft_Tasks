# Rock-Paper-Scissors with Score
import random
choices = ["rock","paper","scissors"]
user_score = 0
computer_score = 0
while True:
    user = input("\nEnter rock/paper/scissors or 'quit' to exit:").lower()
    if user == "quit":
           print("\nFinal score -> you:", user_score, "computer:", computer_score)
           print("Thanks for playing!")
           break
    if user not in choices:
         print("Invalid choice.")
         continue
    comp = random.choice(choices)
    print(f"computer chose: {comp}")
    if user == comp:
         print("It's a tie! ")
    elif(user == "rock" and comp == "scissors") or \
        (user == "paper" and comp == "rock")  or \
        (user == "scissors" and comp == "paper"):
         print("you win this round!") 
         user_score +=1

    else:
          print("computer wins this round!")
          computer_score +=1
          print(f"current score -> you: {user_score} | computer: {computer_score}")
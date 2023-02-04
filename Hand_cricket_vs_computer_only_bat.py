'''
Hand Cricket Computer vs Player only batting
- Abhisek Sarkar
'''

import random

# Initialize the score for each team
team1_score = 0
team2_score = 0

# Get the total overs for the game from the user
overs = int(input("Enter the number of overs: "))

# Each over consists of 6 deliveries
for over in range(overs):
    print(f"Over {over + 1}:")
    
    # The first team bats
    print("You are batting:")
    for delivery in range(6):
        print(f"Delivery {delivery + 1}:")
        team1_run = int(input("Enter runs scored (0-6): "))
        if team1_run == 0:
            print("You are out!")
            break
        team1_score += team1_run
    print(f"Your score: {team1_score}")
    
    # The second team bats
    print("\nComputer is batting:")
    for delivery in range(6):
        print(f"Delivery {delivery + 1}:")
        team2_run = random.randint(0, 6)
        if team2_run == 0:
            print("Computer is out!")
            break
        team2_score += team2_run
        print(f"Computer scores {team2_run} runs")
    print(f"Computer's score: {team2_score}")

# Determine the winner
if team1_score > team2_score:
    print(f"\nYou win! Final score: You {team1_score} - Computer {team2_score}")
elif team2_score > team1_score:
    print(f"\nComputer wins! Final score: Computer {team2_score} - You {team1_score}")
else:
    print(f"\nThe match is tied! Final score: You {team1_score} - Computer {team2_score}")

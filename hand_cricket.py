import random

# Initialize the score for each team
team1_score = 0
team2_score = 0

# Get the total overs for the game from the user
overs = int(input("Enter the number of overs: "))

# Get the user's choice of batting or bowling first
choice = input("Do you want to bat or bowl first? (b/B for bowl, anything else for bat): ")

# Each over consists of 6 deliveries
for over in range(overs):
    print(f"Over {over + 1}:")
    
    # The user bowls if they chose to bowl first
    if choice in ['b', 'B']:
        print("\nYou are bowling:")
        for delivery in range(6):
            print(f"Delivery {delivery + 1}:")
            computer_run = random.randint(0, 6)
            user_predict = int(input("Enter your prediction of computer's run (0-6): "))
            if user_predict == computer_run:
                print("Computer is out!")
                break
            team2_score += computer_run
            print(f"Computer scores {computer_run} runs")
        print(f"Computer's score: {team2_score}")
        
        # The user bats after bowling
        choice = 'bat'
    
    # The user bats if they chose to bat first or just finished bowling
    if choice == 'bat':
        print("\nYou are batting:")
        for delivery in range(6):
            print(f"Delivery {delivery + 1}:")
            team1_run = int(input("Enter runs scored (0-6): "))
            if team1_run == 0:
                print("You are out!")
                break
            team1_score += team1_run
        print(f"Your score: {team1_score}")
        
        # The user bowls after batting
        choice = 'bowl'

# Determine the winner
if team1_score > team2_score:
    print(f"\nYou win! Final score: You {team1_score} - Computer {team2_score}")
elif team2_score > team1_score:
    print(f"\nComputer wins! Final score: Computer {team2_score} - You {team1_score}")
else:
    print(f"\nThe match is tied! Final score: You {team1_score} - Computer {team2_score}")

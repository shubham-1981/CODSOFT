import random
game_items = ["rock", "paper", "scissors"]
user_input = input("Choose any one (rock / paper / scissors): ").lower()
computer_input = random.choice(game_items)
print("Computer choice is:", computer_input)
if user_input == computer_input:
    print("Game tied")
elif user_input == "rock":
    if computer_input == "scissors":
        print("You win the game")
    else:
        print("You lose the game")
elif user_input == "paper":
    if computer_input == "rock":
        print("You win the game")
    else:
        print("You lose the game")
elif user_input == "scissors":
    if computer_input == "paper":
        print("You win the game")
    else:
        print("You lose the game")
else:
    print("Invalid input")

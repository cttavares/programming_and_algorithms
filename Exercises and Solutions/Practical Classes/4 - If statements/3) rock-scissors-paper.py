import random

def rock_paper_scissors(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        return 'Tie!', player_choice, computer_choice
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        return 'Player wins!', player_choice, computer_choice
    elif (player_choice == 'Scissors' and computer_choice == 'Rock') or \
         (player_choice == 'Rock' and computer_choice == 'Paper') or \
         (player_choice == 'Paper' and computer_choice == 'Scissors'):
        return 'Computer wins!', player_choice, computer_choice
    else:
        return 'Invalid play', player_choice, computer_choice

# Example
print ("Rock ? Scissors ? Paper?")
x = input ("Your choice (Rock, Scissors, Paper): ")

print(rock_paper_scissors(x))  # Outputs result, player choice, computer choice

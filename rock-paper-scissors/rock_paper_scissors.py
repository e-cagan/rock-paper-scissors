import random

def play():
    computer_choice = random.choice(['r', 'p', 's'])

    while True:
        player_choice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
        
        if player_choice == 'r' and computer_choice == 's' or player_choice == 'p' and computer_choice == 'r' or player_choice == 's' and computer_choice == 'p':
            print(f"Congrats! You won. Computer's choice was {computer_choice}")
            break
        elif player_choice == 's' and computer_choice == 'r' or player_choice == 'r' and computer_choice == 'p' or player_choice == 'p' and computer_choice == 's':
            print(f"Sorry, you lost. Computer's choice was {computer_choice}")
            break
        elif player_choice == computer_choice:
            print("It's a tie!")
            break
        else:
            print("Invalid choice.")
            break

    user_response = input("Wanna play again? 'yes' or 'no': ").lower()

    if user_response == 'yes':
        play()
    elif user_response == 'no':
        print("Come again sometime :)")
    else:
        print("Invalid response")

play()
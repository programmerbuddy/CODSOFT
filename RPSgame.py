import random

def get_user_choice():
    while True:
        print("select your weapon:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter your choice 1,2 or 3: ")
        if choice in ['1','2','3']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1,2 or 3")
            
def get_computer_choice():
    return random.randint(1,3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "its a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
        (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"
    
def play_game():
    player_score = 0
    computer_score = 0
    
    while True:
        print("\nLet's play Rock-Paper-Scissors!")
        
        while True:
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            choices = ["Rock","Paper","Scissors"]
            print(f"\nYou choose: {choices[user_choice - 1]}")
            print(f"Computer chose: {choices[computer_choice -1]}")
            
            res =  determine_winner(user_choice, computer_choice)
            print(res)
            
            if res == "you win!":
                user_choice += 1
            elif res == "Computer wins!":
                computer_choice += 1
                
            print(f"\nScore- You: {user_choice}, Computer: {computer_choice} ")
            
            play_again = input("\nDo you want to play another chance? (yes/no): ").lower()
            if play_again != "yes!":
                break
            
            while True:
                next_action = input("\nDo you want to play again or Start New game? (play again/new game): ").lower()
                if next_action in ['paly again','new game']:
                    break
                else:
                    print("Invalid Choice. Please enter 'play again' or 'new again'.")
                    
            if next_action == 'new game':
                player_score = 0
                computer_score = 0
                print("Score have been reset. Starting a new game!")
            elif play_again == 'play_again':
                print("Continuing with the current scores.")

        continue_game = input("\nDo you want to continue playing? (yes/no): ").lower()
        if continue_game != 'yes':
            print("Thanks for playing!")
            break

play_game()

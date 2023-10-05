import random

# Function to display slot machine symbols
def display_symbols(symbols):
    print(" ".join(symbols))

# Function to check for winning combinations
def check_win(symbols):
    if symbols[0] == symbols[1] == symbols[2]:
        return True
    return False

# Function to play the slot machine game
def play_slot_machine(money):
    while money > 0:
        print("\nWelcome to the Slot Machine!")
        print(f"Your current balance: ${money}")
        bet = int(input("Place your bet (or enter 0 to quit): "))
        
        if bet == 0:
            print("Thanks for playing! Goodbye!")
            break
        
        if bet > money:
            print("You don't have enough money to place that bet. Try again.")
            continue
        
        symbols = [random.choice(["Cherry", "Seven", "Bar", "Orange"]) for _ in range(3)]
        display_symbols(symbols)
        
        if check_win(symbols):
            winnings = bet * 2
            print(f"Congratulations! You won ${winnings}!")
            money += winnings
        else:
            print("Sorry, you didn't win this time. Try again!")
            money -= bet
    
    if money <= 0:
        print("Sorry, you're out of money. Game over!")

# Main function to start the game
if __name__ == "__main__":
    starting_money = 100  # You can change the initial amount of money here
    play_slot_machine(starting_money)

# File: CS112_A1_T2_3_20230234.py.
# Purpose: It is played by two people with a pile of coins (or other tokens) between them. The players take turns removing 
# coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, …). The player who removes the last coin wins.
# Author: Ezz Eldeen Amr Abd elmonem Ali kandeel
# ID: 20230234

print("Welcome to Subtracting Squares")
print("==============================")
import random
import math

def generate_non_square_number(min_value, max_value):
    pile = random.randint(min_value, max_value)
    while math.isqrt(pile) ** 2 == pile: # Check if the generated number is a perfect square
        pile = random.randint(min_value, max_value)
    return pile

# Function to check if the number is square 
def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n

while True:
    # Making user to choose between manual or random
    choice = input(" Do you want to choose the number of coins manually or generate a random number? (manual or random): ")
    
    if choice.lower() == "manual":
        while True:
            pile = int(input("Enter the initial number of coins in the pile (non-square number): "))
            if not is_perfect_square(pile) and pile > 0:
                break
            else:
                print("Invalid input. Please enter a positive non-square number.")
    elif choice.lower() == "random":
          # Generating a random non-square number within the specified range
        min_coins = int(input("Enter the minimum number of coins: "))
        max_coins = int(input("Enter the maximum number of coins: "))
        pile = generate_non_square_number(min_coins, max_coins)
    else:
        print("Invalid choice. Please enter 'manual' or 'random' and a non square number.")
        continue
    
    if pile > 0:
        while pile > 0:
            print("Number of coins in the pile:", pile)
            # Player 1's turn
            move = int(input("Player 1: Make your subtraction: "))
            if move > 0 and move <= pile and math.isqrt(move) ** 2 == move:
                pile -= move
                print("The number of tokens left:", pile)
            else:
                print("Invalid move. Please enter a non-zero square number of coins (1, 4, 9, 16, …).")
                continue
            
            if pile == 0:
                print("Player 1 wins!")
                break
            
            # Player 2's turn
            move = int(input("Player 2: Make your subtraction: "))
            if move > 0 and move <= pile and math.isqrt(move) ** 2 == move:
                pile -= move
                print("The number of tokens left:", pile)
            else:
                print("Invalid move. Please enter a non-zero square number of coins (1, 4, 9, 16, …).")
                continue
            
            if pile == 0:
                print(" Player 2 wins! ")
                break
    else:
        print("Number of coins in the pile should be greater than 0.")
    
    play_again = input("Do you want to play again? (yes or no): ")
    if play_again.lower() != 'yes':
        print("Thanks for playing!")
        break

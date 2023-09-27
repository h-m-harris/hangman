"""
Version: 2
Purpose: Play hangman
"""

## Install rich first ##  pip install rich
# Import random & sys module
from rich.console import Console
console = Console()
import random
import sys
from rich.table import Table
from rich import box

hangman_guy = [""" """, """ 
_____
|/   |
|   
|    
|    
|    
""",
"""
 ____
|/   |
|   😑
|    
|    
|    
""",
"""
 ____
|/   |
|   😕
|    |
|    |    
|    
""",
"""
 ____
|/   |
|   😟
|   \|
|    |
|    
""",
"""
 ____
|/   |
|   😑
|   \|/
|    |
|    
""",
"""
 ____
|/   |
|   😑
|   \|/
|    |
|   / 
""",
"""
 ____
|/   |
|   😑
|   \|/
|    |
|   / \ 
""",
"""
 ____
|/   |
|   💀
|   /|\ 
|    |
|   | |
"""]


def main():
    """Play hangman game"""
    # Constant for amount of turns
    incorrect = 8
    tries = 0

    # Print heading
    console.print("Hello, Let's play hangman! You will have " + str(incorrect) + " turns!\n", style="bold blue")

    # Print game options
    table = Table(title=None,box=box.DOUBLE_EDGE)
    table.add_column("Number", justify="left", no_wrap=True,style="blue")
    table.add_column("Difficulty", justify="left", no_wrap=True)
    table.add_column("Letters", justify="left", no_wrap=True)
    table.add_row("1", "Easy", "3-5")
    table.add_row("2", "Medium", "6-7")
    table.add_row("3", "Hard", "8-10")
    table.add_row("4", "Expert", "11-14")
    console.print(table)

    while True:
        # Ask user for game choice
        game_choice = input("What game would you like to play? (1-4)" )
    
        if game_choice == "1":
            # open a file in the same folder as the program, random word chosen
            with open("3_5.txt", "r") as text_file:
                word = random.choice(text_file.read().split())
                guesses = ''
                text_file.close()
                break
            
        elif game_choice == "2":
            # open a file in the same folder as the program, random word chosen
            with open("6_7.txt", "r") as text_file:
                word = random.choice(text_file.read().split())
                guesses = ''
                text_file.close()
                break
        elif game_choice == "3":
            # open a file in the same folder as the program, random word chosen
            with open("8_10.txt", "r") as text_file:
                word = random.choice(text_file.read().split())
                guesses = ''
                text_file.close()
                break
        elif game_choice == "4":
            # open a file in the same folder as the program, random word chosen
            with open("11_14.txt", "r") as text_file:
                word = random.choice(text_file.read().split())
                guesses = ''
                text_file.close()
                break
        else:
            print("Please enter a number 1-4.\n")
            continue
            
    # Loop game until no turns are left
    while incorrect > 0:         
        wrong = 0
        for char in word:      
            if char in guesses:    
                print(char, end="") 
            else:
                print("_", end="")     
                wrong += 1    

        # Print blank line
        print()

        # If the game is won
        if wrong == 0:        
            win_text()
            play_again()             

        # Guesses for the game
        guess = ''
        if len(guess) < 1:
            guess = input("\nGuess a character or enter the correct word: ").upper()
        guesses += guess                    

        # If the guess is wrong
        if guess not in word:  
            incorrect -= 1  
            tries += 1
            console.print("Wrong!", style="bold underline red") 
            print("You have", + incorrect, 'incorrect guesses left!')
            print(hangman_guy[tries])
    
            # If there are no turns left
            if incorrect == 0:           
                game_over_text()
                play_again()

        # If the game is won with the word guessed       
        if guess is word:
            win_text()
            play_again() 

def play_again():
    """Gives option to play the game again"""
    print("\nDo you want to play again? (y or n)")
    
    # Convert the player's input() to lower_case
    answer = input("> ").lower()

    if "y" in answer:
        # if player typed "yes" or "y" start the game from the beginning
        main()
    else:
        # if user types anything besides "yes" or "y", exit() the program
        sys.exit()

def game_over_text():
    """Prints when game is lost"""
    console.print("""
   ___   _   __  __ ___    _____   _____ ___ 
  / __| /_\ |  \/  | __|  / _ \ \ / / __| _ \ 
 | (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   /
  \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\ 
                                                                                                    
    """, style="red")  

def win_text():
    """Prints when game is won"""
    console.print("""
 __   __                                _ 
 \ \ / /__  _   _  __      _____  _ __ | |
  \ V / _ \| | | | \ \ /\ / / _ \| '_ \| |
   | | (_) | |_| |  \ V  V / (_) | | | |_|
   |_|\___/ \__,_|   \_/\_/ \___/|_| |_(_)
                                                                                                                         
    """, style="green")  


# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
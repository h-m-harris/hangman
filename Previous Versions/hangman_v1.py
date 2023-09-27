"""
Version:1
Purpose: Play hangman
"""

# Import random & sys module
import random
import sys

def main():
    """Pay hangman game"""
    # Constant for amount of turns
    turns = 10

    # Print heading
    print("\nHello, Let's play hangman! You will have " + str(turns) + " turns!\n")

    # List of words in game, random word chosen
    wordList = [
        "awkward", "bookworm", "crypt", "dwarves", "espionage", "frazzled", "gnarly", "hyphen", "injury", 
        "jumbo", "keyhole", "lucky", "megahertz", "numbskull", "oxidize", "pixel", "queue", "rhythm", 
        "sphinx", "transplant", "unknown", "vaporize", "wimpy", "xylophone", "yippee", "zipper"]
    word = random.choice(wordList)
    guesses = ''

    # Loop game until no turns are left
    while turns > 0:         
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
            guess = input("\nGuess a character or enter the correct word: ")
        guesses += guess                    

        # If the guess is wrong
        if guess not in word:  
            turns -= 1        
            print("Wrong") 
            print("You have", + turns, ' turns left!')
    
            # If there are no turns left
            if turns == 0:           
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
    print("""
   ___   _   __  __ ___    _____   _____ ___ 
  / __| /_\ |  \/  | __|  / _ \ \ / / __| _ \ 
 | (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   /
  \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\ 
                                                                                                    
    """)  

def win_text():
    """Prints when game is won"""
    print("""
 __   __                                _ 
 \ \ / /__  _   _  __      _____  _ __ | |
  \ V / _ \| | | | \ \ /\ / / _ \| '_ \| |
   | | (_) | |_| |  \ V  V / (_) | | | |_|
   |_|\___/ \__,_|   \_/\_/ \___/|_| |_(_)
                                                                                                                         
    """)  

# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
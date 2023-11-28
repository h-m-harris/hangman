"""
Version: Final version
Purpose: Play hangman
"""
# Pip install pygame
# Import modules
import random, sys, pygame
from timeit import default_timer

# Initialize pygame
pygame.init()

# Constants for program
WIDTH = 800
HEIGHT = 700
BORDER = 2
# Constants for colors
grey = (128, 128, 128)
darkgrey = (52, 73, 94)
black = (0, 0, 0)
blue = (167, 193, 245)
# Constants for gameplay
GUESSED = []
BOXES = []
BUTTONS = []
SIZE = 50
ALPHA = 65
hangman_image = 0
game_ending = 0

# Create text font and size for  buttons
title_font = pygame.font.SysFont("Calibri", 70, bold=True)
btn_font = pygame.font.SysFont("Calibri", 50, bold=True)

# Set window size
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    # Set caption & icon for game
    pygame.display.set_caption("Hangman!")
    icon = pygame.image.load("icon.ico")
    pygame.display.set_icon(icon)

    # Set background color of screen
    screen.fill(black)

    # Insert Hangman image for menu
    intro_image = pygame.image.load("hang3.png")
    screen.blit(intro_image,(100,100))
    # Insert game play buttons
    play_again()

def display_text(message, x, y, font):
    # Create text using "message"
    text = font.render(message, 1, blue)
    # Position the rectangle in the correct location using x,y
    rect = text.get_rect(bottomleft = (x, y))
    # Copy the text onto the surface of the rect
    screen.blit(text, rect)
    # Draw the rectangle to the screen
    pygame.draw.rect(screen, darkgrey, rect, 4)
    # Update the screen
    pygame.display.update()
    # Return the rectangle to use with collidepoint for click selection
    return rect

def game_options():
    # Fill the screen
    screen.fill(black)

    # Create text and rectangles with border for each difficulty using "display_text" method
    display_text("Choose a difficulty", x=150, y=150, font=title_font)
    display_text(" Easy: 3-5 Letters ", x=230, y=250, font=btn_font)
    display_text(" Medium: 6-7 Letters ", x=200, y=350, font=btn_font)
    display_text(" Hard: 8-10 Letters ", x=220, y=450, font=btn_font)
    display_text(" Expert: 11-14 Letters ", x=200, y=550, font=btn_font)

    while True:
        # Look for events in the game
        for event in pygame.event.get(): 
            # If game is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If mouse is pressed on a button play with the difficulty chosen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if display_text(" Easy: 3-5 Letters ", x=230, y=250, font=btn_font).collidepoint(event.pos):
                    # Open 3_5.txt in the same folder as the program, random word chosen
                    word_list("3_5.txt")
                if display_text(" Medium: 6-7 Letters ", x=200, y=350, font=btn_font).collidepoint(event.pos):
                    # Open 6_7.txt in the same folder as the program, random word chosen
                    word_list("6_7.txt")
                if display_text(" Hard: 8-10 Letters ", x=220, y=450, font=btn_font).collidepoint(event.pos):
                    # Open 8_10.txt in the same folder as the program, random word chosen
                    word_list("8_10.txt")
                if display_text(" Expert: 11-14 Letters ", x=200, y=550, font=btn_font).collidepoint(event.pos):
                    # Open 11_14.txt in the same folder as the program, random word chosen
                    word_list("11_14.txt")

        # Update the screen
        pygame.display.update()

def word_list(file):
    # Open file and select a random word to play the game
    with open(file, "r") as text_file:
            word = random.choice(text_file.read().split())
            play_game(word)
            text_file.close()

def make_alphabet():
    # Create 2 rows of 13 letters for the alphabet
    for row in range(2):
        for col in range(13):
            x = 20+(60 * col)
            y = 500+(60 * row)
            # Create squares around the alphabet
            box = pygame.Rect(x,y,SIZE,SIZE)
            BOXES.append(box)
            
    # Append the alphabet to the boxes
    for index, box in enumerate(BOXES):
        button = ([box, chr(ALPHA+index)])
        BUTTONS.append(button)

def draw_buttons():
    # Draw alphabet buttons to the screen
    for button, letter in BUTTONS:
        btn_text = btn_font.render(letter, True, blue)
        btn_text_rect = btn_text.get_rect(center=(button.x + SIZE//2, button.y + SIZE//2))
        pygame.draw.rect(screen, darkgrey, button, 3)
        screen.blit(btn_text, btn_text_rect)
    
def display_word(word):
    word_guess = ""
    # If the character has been guessed, show the character
    for char in word:      
        if char in GUESSED:    
            word_guess += char + " "
        # If the character has not been guessed, show "_"
        else:
            word_guess += "_ "  
    draw_hangman(word)
    # Show word_guess or dashes on the screen
    display_word_dash = title_font.render(word_guess, True, grey)
    screen.blit(display_word_dash, (((WIDTH / 2)-(len((word_guess*12)))), 350))

def draw_hangman(word):
    # Add container for images
    images = []
    # Set range for images displayed (10 tries)
    for i in range(11):
        image = pygame.image.load(f"hangman{i}.png")
        images.append(image)
        # At 10 tries, end game
        if hangman_image == 10:
            game_endings(game_ending + 1, word)
    # Update the hangman guy on the screen
    return screen.blit(images[hangman_image], (100, 25))    

def game_endings(game_ending, word):

    while True:
        # Look for events in the game and close game if "X" is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Set the background color to Black
        screen.fill(black)

        if game_ending == 1:
            # Stop the game timer
            time_end = default_timer()
            # Load the dead hangman on the screen
            image = pygame.image.load(f"hangman10.png")
            screen.blit(image, (100, 190))
            # Create text Lost
            display_text(" You Lost! ", x=250, y=100, font=title_font)
            # Display the time playing the game (end-start to calculate total seconds)
            display_text(f" Time taken: {round(time_end - time_start)} seconds ", x=160, y=170, font=btn_font)
            # Display the correct word
            display_text(f" The word was: {word}  ", x=((WIDTH / 4)-(len((word*10)))), y=520, font=btn_font)
            # Display play/quit buttons
            play_again()
            # Update the screen
            pygame.display.update()

        if game_ending == 2:
            # Stop the game timer
            time_end = default_timer()
            # Create text Won!
            display_text(" You Won!  ", x=250, y=200, font=title_font)
            # Display the time playing the game (end-start to calculate total seconds)
            display_text(f" Time taken: {round(time_end - time_start)} seconds ", x=160, y=350, font=btn_font)
            # Display the correct word
            display_text(f" The word was: {word}  ", x=((WIDTH / 4)-(len((word*10)))), y=475, font=btn_font)
            # Display play/quit buttons
            play_again()
            # Update the screen
            pygame.display.update()

def play_again():
    global GUESSED
    # Create text for play again menu buttons
    display_text(" Quit Game ", x=450, y=600, font=btn_font)
    display_text(" Play Game ", x=100, y=600, font=btn_font)

    while True:
        # Look for events in the game
        for event in pygame.event.get(): 
            # If game is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If mouse is pressed on a button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if display_text(" Quit Game ", x=450, y=600, font=btn_font).collidepoint(event.pos):
                    # Exit button
                    pygame.quit()
                    sys.exit()
                if display_text(" Play Game ", x=100, y=600, font=btn_font).collidepoint(event.pos):
                    # Play game button
                    reset_game()
                    game_options()
        # Update game
        pygame.display.update()

def reset_game():
    # Access game variables and reset them for a new game
    global GUESSED, BUTTONS, BOXES, hangman_image
    GUESSED = []
    BUTTONS = []
    BOXES = []
    hangman_image = 0

def play_game(word):
    global hangman_image, time_start
    # Make the alphabet buttons
    make_alphabet()
    # Start the timer to trak gameplay time
    time_start = default_timer()
    while True:
        # Look for events in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # If mouse is pressed on an alphabet button
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button, letter in BUTTONS:
                    if button.collidepoint(event.pos):
                        # Add the guessed letter to GUESSED list
                        GUESSED.append(letter)
                        # MAke the guessed letter disappear
                        BUTTONS.remove([button, letter])
                        # If the letter isn"t in word, Add a limb
                        if letter not in word:
                            hangman_image +=1

        # Boolean for game winning            
        game_won = True
        # Check to see if the correct letters are guessed
        for letter in word:
            if letter not in GUESSED:
                game_won = False
        # If the game is won, Show results
        if game_won:
            game_endings(game_ending + 2, word)

        # Set Background color to Black
        screen.fill(black)

        # Call Draw buttons and word to screen
        draw_buttons()
        display_word(word)

        # Update the screen
        pygame.display.update()

# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
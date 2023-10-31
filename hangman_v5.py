"""
Version: V5 - Working version
Purpose: Play hangman
"""
# Pip install pygame
# Import modules
import random, sys, pygame

# Initialize pygame
pygame.init()

# Constants for program
WIDTH = 800
HEIGHT = 700
BORDER = 2
grey = (128, 128, 128)
darkgrey = (52, 73, 94)
black = (0, 0, 0)
blue = (167, 193, 245)
GUESSED = []
BOXES = []
BUTTONS = []
SIZE = 50
ALPHA = 65

# Create text font and size for  buttons
option_font = pygame.font.SysFont('Calibri', 40, bold=True)
title_font = pygame.font.SysFont('Calibri', 70, bold=True)
menu_font = pygame.font.SysFont('Calibri', 32, bold=True)
btn_font = pygame.font.SysFont('Calibri', 50)

# Set window size
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    # Set caption & icon for game
    pygame.display.set_caption("Hangman!")
    icon = pygame.image.load('icon.ico')
    pygame.display.set_icon(icon)

    # Go to the menu            
    main_menu()

def main_menu():
    # Set background color of screen
    screen.fill(black)

    # Insert Hangman image for menu
    intro_image = pygame.image.load('hang3.png')
    screen.blit(intro_image,(100,100))

    # Create text for main menu buttons
    menu_font = pygame.font.SysFont('Calibri', 32, bold=True)
    quit_text = menu_font.render(" Quit Game ", True, blue)
    play_text = menu_font.render(" Play Game ", True, blue)

    # Create rectangles with border
    quit_rect = quit_text.get_rect(bottomleft = (500 , 600))
    play_rect = play_text.get_rect(bottomleft = (200 , 600))
    screen.blit(quit_text, quit_rect)
    pygame.draw.rect(screen, darkgrey,quit_rect, BORDER)
    screen.blit(play_text , play_rect)
    pygame.draw.rect(screen, darkgrey, play_rect,BORDER)

    while True:
        # Look for events in the game
        for event in pygame.event.get(): 
            # If game is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If mouse is pressed on a button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(event.pos):
                    # Exit button
                    pygame.quit()
                    sys.exit()
                if play_rect.collidepoint(event.pos):
                    # Play game button
                    game_options()

        # Update game
        pygame.display.update()

def game_options():
    # Fill the screen
    screen.fill(black)

    # Create text font and size for main menu buttons
    option_font = pygame.font.SysFont('Calibri', 40, bold=True)

    # Create text and rectangles with border for each difficulty
    difficulty = title_font.render(" Choose a difficulty: ", True, blue)
    diff_rect = difficulty.get_rect(bottomleft = (100 , 150))
    screen.blit(difficulty, diff_rect)
    pygame.draw.rect(screen, darkgrey, diff_rect, 4)

    easy_text = option_font.render(" Easy: 3-5 Letters ", True, blue)
    easy_rect = easy_text.get_rect(bottomleft = (230 , 250))
    screen.blit(easy_text, easy_rect)
    pygame.draw.rect(screen, darkgrey, easy_rect, 3)

    med_text = option_font.render(" Medium: 6-7 Letters ", True, blue)
    med_rect = med_text.get_rect(bottomleft = (200 , 350))
    screen.blit(med_text , med_rect)
    pygame.draw.rect(screen, darkgrey, med_rect,3)

    hard_text = option_font.render(" Hard: 8-10 Letters ", True, blue)
    hard_rect = hard_text.get_rect(bottomleft = (220 , 450))
    screen.blit(hard_text, hard_rect)
    pygame.draw.rect(screen, darkgrey, hard_rect, 3)

    expert_text = option_font.render(" Expert: 11-14 Letters ", True, blue)
    expert_rect = expert_text.get_rect(bottomleft = (200 , 550))
    screen.blit(expert_text , expert_rect)
    pygame.draw.rect(screen, darkgrey, expert_rect,3)

    while True:
        # Look for events in the game
        for event in pygame.event.get(): 
            # If game is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If mouse is pressed on a button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    # Open 3_5.txt in the same folder as the program, random word chosen
                    with open("3_5.txt", "r") as text_file:
                        word = random.choice(text_file.read().split())
                        play_game(word)
                        text_file.close()
                if med_rect.collidepoint(event.pos):
                    # Open 6_7.txt in the same folder as the program, random word chosen
                    with open("6_7.txt", "r") as text_file:
                        word = random.choice(text_file.read().split())
                        play_game(word)
                        text_file.close()
                if hard_rect.collidepoint(event.pos):
                    # Open 8_10.txt in the same folder as the program, random word chosen
                    with open("8_10.txt", "r") as text_file:
                        word = random.choice(text_file.read().split())
                        play_game(word)
                        text_file.close()
                if expert_rect.collidepoint(event.pos):
                    # Open 11_14.txt in the same folder as the program, random word chosen
                    with open("11_14.txt", "r") as text_file:
                        word = random.choice(text_file.read().split())
                        play_game(word)
                        text_file.close()
        # Update the screen
        pygame.display.update()

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
    
    # Show word_guess or dashes on the screen
    display_word_dash = title_font.render(word_guess, True, grey)
    screen.blit(display_word_dash, (((WIDTH / 2)-(len((word_guess*12)))), 400))

def play_game(word):
    make_alphabet()
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
                        GUESSED.append(letter)
                        BUTTONS.remove([button, letter])
                        
        screen.fill(black)
        draw_buttons()
        display_word(word)

        pygame.display.update()


# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
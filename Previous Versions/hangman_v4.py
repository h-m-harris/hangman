"""
Version: Working version
Purpose: Play hangman
"""
# Pip install pygame
# Import modules
import random
import sys
import pygame

# Initialize pygame
pygame.init()

# Constants for program
WIDTH = 800
HEIGHT = 700
BORDER = 2
grey = (128, 128, 128)
bluegray = (115, 147, 179)
darkgrey = (52, 73, 94)
black = (0, 0, 0)
blue = (167, 193, 245)

# Set window size
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    # Set window size
    pygame.display.set_caption("Hangman!")

    # Set icon for game
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
    title_font = pygame.font.SysFont('Calibri', 70, bold=True)

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
                    # Play game button
                    gp_easy()
                if med_rect.collidepoint(event.pos):
                    # Play game button
                    gp_medium()
                if hard_rect.collidepoint(event.pos):
                    # Play game button
                    gp_hard()
                if expert_rect.collidepoint(event.pos):
                    # Play game button
                    gp_expert()
        # Update the screen
        pygame.display.update()

def gp_easy():
    global word, guesses
    # open a file in the same folder as the program, random word chosen
    with open("3_5.txt", "r") as text_file:
        word = random.choice(text_file.read().split())
        guesses = ''
        play_game(word, guesses)
        text_file.close()
                    
def gp_medium():
    global word, guesses
    # open a file in the same folder as the program, random word chosen
    with open("6_7.txt", "r") as text_file:
        word = random.choice(text_file.read().split())
        guesses = ''
        play_game(word, guesses)
        text_file.close()
                    
def gp_hard():
    global word, guesses
    # open a file in the same folder as the program, random word chosen
    with open("8_10.txt", "r") as text_file:
        word = random.choice(text_file.read().split())
        guesses = ''
        play_game(word, guesses)
        text_file.close()
                    
def gp_expert():
    global word, guesses
    # open a file in the same folder as the program, random word chosen
    with open("11_14.txt", "r") as text_file:
        word = random.choice(text_file.read().split())
        guesses = ''
        play_game(word, guesses)
        text_file.close()

def play_game(word, guesses):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(darkgrey)
        # Create text "Coming soon"
        CS_font = pygame.font.SysFont('Calibri', 60, bold=True)
        CS_text = CS_font.render(" Coming soon... ", True, blue)

        # Create rectangle with border
        CS_rect = CS_text.get_rect(topleft = (200 , 350))
        screen.blit(CS_text, CS_rect)
        pygame.draw.rect(screen, darkgrey,CS_rect, BORDER)
        pygame.display.update()


# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
"""
Version: 3
Purpose: Play hangman
"""
# Pip install pygame
# Import modules
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

def main():
    global clock, screen
    clock = pygame.time.Clock()

    # Set window size and caption
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
                    play_game()

        # Update game
        pygame.display.update()

def play_game():
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
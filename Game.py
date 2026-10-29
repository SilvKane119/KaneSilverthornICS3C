import pygame
import time
import random

pygame.init()

# Create the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Square")

# Set up our colours
SKY_BLUE = (135, 206, 235)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (62, 247, 62)
YELLOW = (255, 255, 0)

# Store the player's and enemy starting position
player_x = 375
player_y = 275

enemy1_x = 100
enemy1_y = 200

enemy2_x = 550
enemy2_y = 350

# Fixed bullet coordinates (were swapped in original)
bullet_x = player_x
bullet_y = player_y
bullet_speed = 10 
bullet_active = False

# Control how many pixels the square moves each frame
speed = 3
enemy_speed = 1
enemy_speed2 = 1.3

# Keep the game running
running = True
clock = pygame.time.Clock()

while running:
    # Check for events, including closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keyboard keys are being pressed
    keys = pygame.key.get_pressed()
    
    # Move left/right/up/down
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= speed
    if keys[pygame.K_RIGHT] and player_x < 750:
        player_x += speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= speed
    if keys[pygame.K_DOWN] and player_y < 550:
        player_y += speed

    # Shooting mechanics (Space bar)
    if keys[pygame.K_SPACE]:
        if not bullet_active:
            bullet_x = player_x + 21  # Center the bullet relative to player width (50)
            bullet_y = player_y
            bullet_active = True

    if bullet_active:
        bullet_y -= bullet_speed
        # Deactivate if it goes off-screen
        if bullet_y < 0:
            bullet_active = False

    # Enemy 1 tracking logic
    if enemy1_x < player_x:
        enemy1_x += enemy_speed
    elif enemy1_x > player_x:
        enemy1_x -= enemy_speed

    if enemy1_y < player_y:
        enemy1_y += enemy_speed2
    elif enemy1_y > player_y:
        enemy1_y -= enemy_speed2

    # Enemy 2 tracking logic
    if enemy2_x < player_x:
        enemy2_x += enemy_speed2
    elif enemy2_x > player_x:
        enemy2_x -= enemy_speed2

    if enemy2_y < player_y:
        enemy2_y += enemy_speed
    elif enemy2_y > player_y:
        enemy2_y -= enemy_speed

    # Rects for collision detection
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    enemy1_rect = pygame.Rect(enemy1_x, enemy1_y, 30, 30)
    enemy2_rect = pygame.Rect(enemy2_x, enemy2_y, 30, 30)
    bullet_rect = pygame.Rect(bullet_x, bullet_y, 7, 25)

    # Player collision with enemies (Game Over)
    if player_rect.colliderect(enemy1_rect) or player_rect.colliderect(enemy2_rect):
        pygame.display.set_caption("YOU LOSE")
        pygame.display.flip()
        time.sleep(2)
        running = False

    # Bullet collision with enemies
    if bullet_active and bullet_rect.colliderect(enemy1_rect):
        enemy1_x = random.randint(0, 770)
        enemy1_y = random.randint(0, 570)
        bullet_active = False

    if bullet_active and bullet_rect.colliderect(enemy2_rect):
        enemy2_x = random.randint(0, 770)
        enemy2_y = random.randint(0, 570)
        bullet_active = False

    # Paint the background to clear the previous frame
    screen.fill(SKY_BLUE)

    # Draw game objects
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy1_rect)
    pygame.draw.rect(screen, GREEN, enemy2_rect)
    
    if bullet_active:
        pygame.draw.rect(screen, YELLOW, bullet_rect)

    # Show the updated screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
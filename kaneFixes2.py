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
GREY = (212, 212, 212)
GOLD = (255, 205, 0)
ORANGE =(255, 155, 0)

# Store the player's and enemy starting position
player_x = 375
player_y = 275

enemy1_x = 100
enemy1_y = 200

enemy2_x = 550
enemy2_y = 350

enemy_difficulty = 0

# Power Up Defining & Variables
kill = 0
wide_bullet = False
tall_bullet = False
speed_up = False

power_up_active = False
power_up_type = 0
power_up_x = 0
power_up_y = 0
power_up_rect = None

# Bullet variables
bullet_x = player_x
bullet_y = player_y
bullet_speed = 10 
bullet_active = False
bullet_direction = "up"
last_direction = "up"
bullet_width = 7
bullet_height = 7

# Control how many pixels the square moves each frame
speed = 3

enemy_speed = 0.7
if enemy_difficulty == 5:
    enemy_speed = enemy_speed + 0.2
if enemy_difficulty == 10:
    enemy_speed = enemy_speed + 0.3
if enemy_difficulty == 20:
    enemy_speed = enemy_speed + 0.5

enemy_speed2 = 0.9
if enemy_difficulty == 5:
    enemy_speed2 = enemy_speed2 + 0.2
if enemy_difficulty == 10:
    enemy_speed2 = enemy_speed2 + 0.3
if enemy_difficulty == 20:
    enemy_speed2 = enemy_speed2 + 0.5

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
        last_direction = "left"
    if keys[pygame.K_RIGHT] and player_x < 750:
        player_x += speed
        last_direction = "right"
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= speed
        last_direction = "up"
    if keys[pygame.K_DOWN] and player_y < 550:
        player_y += speed
        last_direction = "down"

    # Shooting mechanics (Space bar)
    if keys[pygame.K_SPACE]:
        if not bullet_active:
            bullet_direction = last_direction  # Lock in the direction it was fired
            if bullet_direction == "up":
                bullet_x = player_x + 21
                bullet_y = player_y
            elif bullet_direction == "down":
                bullet_x = player_x + 21
                bullet_y = player_y + 50
            elif bullet_direction == "left":
                bullet_x = player_x
                bullet_y = player_y + 21
            elif bullet_direction == "right":
                bullet_x = player_x + 50
                bullet_y = player_y + 21
            bullet_active = True

    # Continuous bullet movement every frame if active
    if bullet_active:
        if bullet_direction == "up":
            bullet_y -= bullet_speed
        elif bullet_direction == "down":
            bullet_y += bullet_speed
        elif bullet_direction == "left":
            bullet_x -= bullet_speed
        elif bullet_direction == "right":
            bullet_x += bullet_speed

        # Deactivate if it goes off-screen in any direction
        if bullet_y < 0 or bullet_y > 600 or bullet_x < 0 or bullet_x > 800:
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
    bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)

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
        kill += 1
        enemy_difficulty += 1
        bullet_active = False

    if bullet_active and bullet_rect.colliderect(enemy2_rect):
        enemy2_x = random.randint(0, 770)
        enemy2_y = random.randint(0, 570)
        kill += 1
        enemy_difficulty += 1
        bullet_active = False

    # Power Up Spawning Logic (Spawns once when kill count >= 10 and no power up is currently out)
    if kill >= 10 and not power_up_active:
        power_up_type = random.randint(1, 3)
        power_up_x = random.randint(50, 750)
        power_up_y = random.randint(50, 550)
        power_up_rect = pygame.Rect(power_up_x, power_up_y, 18, 18)
        power_up_active = True

    # Power-Up Collection Collision Check
    if power_up_active and player_rect.colliderect(power_up_rect):
        if power_up_type == 1:
            speed += 2  # Speed up power-up
        elif power_up_type == 2:
            tall_bullet = True
            bullet_height = 20  # Tall bullet power-up
        elif power_up_type == 3:
            wide_bullet = True
            bullet_width = 20  # Wide bullet power-up
        
        power_up_active = False
        kill = 0  # Reset kills so power-ups can spawn again later

    # Paint the background to clear the previous frame
    screen.fill(GREY)

    # Draw game objects
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy1_rect)
    pygame.draw.rect(screen, GREEN, enemy2_rect)
    
    if bullet_active:
        pygame.draw.rect(screen, YELLOW, bullet_rect)

    # Draw the power-up if it is currently active on the map
    if power_up_active:
        if power_up_type == 1:
            pygame.draw.circle(screen, SKY_BLUE, (power_up_x, power_up_y), 9)
        elif power_up_type == 2:
            pygame.draw.circle(screen, GOLD, (power_up_x, power_up_y), 9)
        elif power_up_type == 3:
            pygame.draw.circle(screen, ORANGE, (power_up_x, power_up_y), 9)

    # Show the updated screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
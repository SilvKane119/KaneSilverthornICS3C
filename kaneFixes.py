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

#Power Up Defining
kill = 0

wide_bullet = False

tall_bullet = False

speed_up = False

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
if speed_up == True:
    speed = speed + 2
    speed_up = False

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
    
    # Move left/right/up/down (Fixed '==' to '=')
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

# Saving For Later To Copy And Paste Because Pygame Is Stupid About Circles
#    speed_circle = pygame.draw.circle(screen, SKY_BLUE, (400, 300), 9)
#    tall_circle = pygame.draw.circle(screen, GOLD, (400, 300), 9)
#    wide_circle = pygame.draw.circle(screen, ORANGE, (400, 300), 9)
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
        kill == kill + 1
        enemy_difficulty == enemy_difficulty + 1
        bullet_active = False

    if bullet_active and bullet_rect.colliderect(enemy2_rect):
        enemy2_x = random.randint(0, 770)
        enemy2_y = random.randint(0, 570)
        kill == kill + 1
        bullet_active = False

    # Paint the background to clear the previous frame
    screen.fill(GREY)

    # Draw game objects
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy1_rect)
    pygame.draw.rect(screen, GREEN, enemy2_rect)
    
    if bullet_active:
        pygame.draw.rect(screen, YELLOW, bullet_rect)

# Power Up Spawning
    if kill >= 10:
        power_up = random.randint(1, 3)
        if power_up == 1:
            speed_circle = pygame.draw.circle(screen, SKY_BLUE, (random.randint(0, 800), random.randint(0, 600)), 9)
        elif power_up == 2:
            tall_circle = pygame.draw.circle(screen, GOLD, (random.randint(0, 800), random.randint(0, 600)), 9)
        elif power_up == 3:
            wide_circle = pygame.draw.circle(screen, ORANGE, (random.randint(0, 800), random.randint(0, 600)), 9)
    # Show the updated screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
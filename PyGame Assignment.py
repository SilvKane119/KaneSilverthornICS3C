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
MAROON = (166, 0, 0)
MAGENTA = (238, 0, 255)
BOSSC1 = (212, 202, 202)
BOSSC2 = (212, 190, 190)
BOSSC3 = (212, 174, 174)
BOSSC4 = (199, 148, 148)
BOSSC5 = (181, 129, 129)

# Store the player's and enemy starting position
enemy1_spawn = 1
enemy2_spawn = 1

player_x = 375
player_y = 275

player_width = 50
player_height = 50

enemy1_x = 100
enemy1_y = 200

enemy2_x = 550
enemy2_y = 350

boss_x = 375
boss_y = -80
boss_hp = 30
# Difficulty Defining
enemy_difficulty = 0
hard1 = False
hard2 = False
hard3 = False

# Boss Defining
boss_spawn = 0
boss_battle = False

# Power Up Defining & Variables
kill = 0
wide_bullet = False
tall_bullet = False
speed_up = False
player_shrink = False

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

enemy_speed2 = 0.9

boss_speed = 0.5

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
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    enemy1_rect = pygame.Rect(enemy1_x, enemy1_y, 30, 30)
    enemy2_rect = pygame.Rect(enemy2_x, enemy2_y, 30, 30)
    bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
    boss_rect = pygame.Rect(boss_x, boss_y, 70, 70)
    # Player collision with enemies (Game Over)
    if player_rect.colliderect(enemy1_rect) or player_rect.colliderect(enemy2_rect):
        pygame.display.set_caption("YOU LOSE")
        pygame.display.flip()
        time.sleep(2)
        running = False

    # Bullet collision with enemies
    if bullet_active and bullet_rect.colliderect(enemy1_rect):
        enemy1_spawn = random.randint(1, 4)
        if enemy1_spawn == 1:
            enemy1_x = random.randint(-10, 810)
            enemy1_y = random.randint(-20, -10)
        elif enemy1_spawn == 2:
            enemy1_x = random.randint(810, 820)
            enemy1_y = random.randint(-10, 610)
        elif enemy1_spawn == 3:
            enemy1_x = random.randint(-10, 810)
            enemy1_y = random.randint(610, 620)
        elif enemy1_spawn == 4:
            enemy1_x = random.randint(-20, -10)
            enemy1_y = random.randint(-10, 610)
        kill += 1
        bullet_active = False

    if bullet_active and bullet_rect.colliderect(enemy2_rect):
        enemy2_spawn = random.randint(1, 4)
        if enemy2_spawn == 1:
            enemy2_x = random.randint(-10, 810)
            enemy2_y = random.randint(-20, -10)
        elif enemy2_spawn == 2:
            enemy2_x = random.randint(810, 820)
            enemy2_y = random.randint(-10, 610)
        elif enemy2_spawn == 3:
            enemy2_x = random.randint(-10, 810)
            enemy2_y = random.randint(610, 620)
        elif enemy2_spawn == 4:
            enemy2_x = random.randint(-20, -10)
            enemy2_y = random.randint(-10, 610)
        kill += 1
        bullet_active = False

    # Enemy Difficulty Increase
    if enemy_difficulty == 1:
        hard1 = True
    if enemy_difficulty == 2:
        hard2 = True
    if enemy_difficulty == 3:
        hard3 = True

    if hard1 == True:
        enemy_speed = 0.9
        enemy_speed2 = 1.1
        hard1 == False
    if hard2 == True:
        enemy_speed = 1.2
        enemy_speed = 1.4
        hard2 == False
    if hard3 == True:
        enemy_speed = 1.7
        enemy_speed2 = 1.9
        hard3 == False

    # Power Up Spawning Logic (Spawns once when kill count >= 10 and no power up is currently out)
    if kill >= 10 and not power_up_active:
        power_up_type = random.randint(1, 5)
        power_up_x = random.randint(50, 750)
        power_up_y = random.randint(50, 550)
        power_up_rect = pygame.Rect(power_up_x, power_up_y, 18, 18)
        power_up_active = True

    # Power-Up Collection Collision Check
    if power_up_active and player_rect.colliderect(power_up_rect):
        if power_up_type == 1:
            speed += 0.7  # Speed up power-up
        elif power_up_type == 2:
            tall_bullet = True
            bullet_height += 4  # Tall bullet power-up
        elif power_up_type == 3:
            wide_bullet = True
            bullet_width += 4  # Wide bullet power-up
        elif power_up_type == 4:
            player_height -= 4  # Player Shrink power-up
            player_width -= 4
        elif power_up_type == 5:
            bullet_speed += 3. # Bullet Speed power-up
        if boss_battle == False:
            boss_spawn += 1
        power_up_active = False
        kill = 0  # Reset kills so power-ups can spawn again later

    # Boss Screen Darkening
    if boss_spawn == 1:
        screen.fill(BOSSC1)
    elif boss_spawn == 2:
        screen.fill(BOSSC2)
    elif boss_spawn == 3:
        screen.fill(BOSSC3)
    elif boss_spawn == 4:
        screen.fill(BOSSC4)
    elif boss_spawn == 5:
        screen.fill(BOSSC5)
        boss_battle = True
    else:
        screen.fill(GREY)

    # Everything Relating To The Boss vvv
    if boss_battle == True:

        boss_x == 375
        boss_y == -80

        # Boss Tracking Logic
        if boss_x < player_x:
            boss_x += boss_speed
        elif boss_x > player_x:
            boss_x -= boss_speed
            
        if boss_y < player_y:
            boss_y += boss_speed
        elif boss_y > player_y:
            boss_y -= boss_speed

        pygame.draw.rect(screen, MAROON, boss_rect)
        if bullet_active and bullet_rect.colliderect(boss_rect):
            boss_hp = boss_hp - 1
            bullet_active = False

        # Player Dying To Boss
        if player_rect.colliderect(boss_rect):
            pygame.display.set_caption("YOU LOSE")
            pygame.display.flip()
            time.sleep(2)
            running = False

        # Boss Defeat
        if boss_hp <= 0:
            boss_battle = False
            enemy_difficulty += 1
            boss_spawn == 0
            boss_x == 375
            boss_y == -80
            
    # Draw game objects
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy1_rect)
    pygame.draw.rect(screen, RED, enemy2_rect)
    
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
        elif power_up_type == 4:
            pygame.draw.circle(screen, MAGENTA, (power_up_x, power_up_y), 9)
        elif power_up_type == 5:
            pygame.draw.circle(screen, YELLOW, (power_up_x, power_up_y), 9)

    # Show the updated screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
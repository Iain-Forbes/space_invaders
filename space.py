import pygame
import random

pygame.init()

#Create Screen
screen = pygame.display.set_mode((800, 600))

#Background
# background = pygame.image.load()

# Change Window Caption, Icon 
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player w\ static start point 
playerImg = pygame.image.load('jet.png')
playerX = 390
playerY = 490

playerX_change = 0

#Enemy w\ randomised positioning
enemyImg = pygame.image.load('ufo_2.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)

enemyX_change = 0.1
enemyY_change = 40


##Draw Player Function
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game Looop
RUNNING= True
while RUNNING:
    screen.fill((30, 16, 25)) #RGB Do before everything has drawn
    #Add Background
    # screen.blit(background,(0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    # Move Left or Right if, changes playerX location (playerX += playerX_change)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                

    #Player/Enenmy can't escape window, rests position + movement  
    playerX += playerX_change
    if playerX <=0:
        playerX = 0
    elif playerX >=760:
        playerX = 760

    enemyX += enemyX_change
    if enemyX <=0:
        enemyX_change = 0.1
        enemyY += enemyY_change
    elif enemyX >=740:
        enemyX_change = -0.1
        enemyY += enemyY_change

   

    #Function calls
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    
    #Window Refresh
    pygame.display.update()
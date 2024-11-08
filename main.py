import pygame
import random
import math
from pygame import mixer

#Initialize the game
pygame.init()

#afficher un écran avec les dimensions
#screen qui s'affiche et se ferme instant
screen = pygame.display.set_mode((800,900))

#Ajouter une image en background
background = pygame.image.load("images/background.png")

#Ajouter un son en fond
mixer.music.load("sounds/Pixel Love.mp3")
mixer.music.play(-1)

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

#Player image
playerImg = pygame.image.load("images/player.png")
#Coordonnées d'apparition de l'icone du joueur
playerX = 370
playerY = 810
#Variable de mouvement
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 15

#Enemy image
for i in range(num_of_enemies):
  enemyImg.append(pygame.image.load("images/enemy.png"))
  enemyX.append(random.randint(0, 736))
  enemyY.append(random.randint(50, 150))
  #Variable de mouvement
  enemyX_change.append(2)
  enemyY_change.append(70)

#Bullet image
bulletImg = pygame.image.load("images/bullet.png")
#Coordonnées d'apparition de l'icone de l'enemie
bulletX = 0
bulletY = 810
#Variable de mouvement
bulletX_change = 0
bulletY_change = 8
#Ready - L'image est invisible à l'écran
#Fire  - L'image se met en mouvement
bullet_state = "ready"

#Score value
score_value = 0
font = pygame.font.Font('font/JetBrainsMono.ttf', 32)
textX = 10
textY = 10

def show_score(x, y):
  score = font.render("Score: " + str(score_value), True, (255, 255, 255))
  screen.blit(score, (x, y))

def player(x, y):
  #Faire apparaitre l'image à l'écran
  screen.blit(playerImg, (x, y))

def enemy(x, y, i):
  #Faire apparaitre l'image à l'écran
  screen.blit(enemyImg[i], (x, y))
  
def fire_bullet(x, y):
  #Pour que la valeur soit accessible
  global bullet_state  
  bullet_state = "fire"
  #Plus 16 et 10 pour faire en sorte que la balle soit au centre du spaceship
  screen.blit(bulletImg, (x + 16, y + 10))
  
def isCollision(enemyX, enemyY, bulletX, bulletY):
  distance = math.sqrt(math.pow(bulletX - enemyX, 2) + math.pow(bulletY - enemyY, 2))
  if distance < 27:
    return True
  else:
    return False 

running = True
while running:
  #Ajouter une couleur à notre background    
  screen.fill((25, 25, 25, 0.5))
  #Background image
  screen.blit(background, (0, 0))
  
  #event = tout les inputs faits par l'utilisateur
  for event in pygame.event.get():
    #quand l'input correspond à la fermeture de fenetre, on break la loop
    if event.type == pygame.QUIT:
      running = False
  #Check si on appuie à droite ou gauche
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
      playerX_change = -2.5
    if event.key == pygame.K_RIGHT:
      playerX_change = 2.5
    if event.key == pygame.K_UP:
      #Condition pour que la balle ne soit pas redirigé sur la position du player
      if bullet_state == "ready":
        bullet_Sound = mixer.Sound("sounds/shoot.wav")
        bullet_Sound.play()
        bulletX = playerX
        fire_bullet(bulletX, bulletY)  
  #Touche relachée    
  if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
      playerX_change = 0
  #Une méthode un peu layer, le player après le screen pour qu'il se superpose
  #Verification pour que le joueur ne dépasse pas les limites de l'écran
  playerX += playerX_change
  if playerX <= 0:
    playerX = 0
  elif playerX >= 736:
    playerX = 736  
    
  #Verification pour que l'enemie ne dépasse pas les limites de l'écran  
  for i in range(num_of_enemies):
    enemyX[i] += enemyX_change[i]
    if enemyX[i] <= 0:
      enemyX_change[i] = 2
      enemyY[i] += enemyY_change[i]
    elif enemyX[i] >= 736:
      enemyX_change[i] = -2
      enemyY[i] += enemyY_change[i] 
    #Check collision
    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
      hit_Sound = mixer.Sound("sounds/hit.mp3")
      hit_Sound.play()
      bulletY = 810
      bullet_state = "ready"  
      score_value += 1
      enemyX[i] = random.randint(0, 735)
      enemyY[i] = random.randint(50, 150)  
    enemy(enemyX[i], enemyY[i], i)  
  
  #Vérification quand la balle atteint le haut de l'écran
  if bulletY <= 0:
    bulletY = 810
    bullet_state = "ready"  
    
  #Bullet movement
  if bullet_state == "fire":
    fire_bullet(bulletX, bulletY)
    bulletY = bulletY - bulletY_change  
    
  #Affichage de la nouvelle position après modification  
  player(playerX, playerY)
  #Afficher le score à l'écran
  show_score(textX, textY)
  #On a besoin d'update sinon les changements ne vont pas s'appliquer
  pygame.display.update()    
import js as p5
from classes import *
from movement import *
import random

print('Assignment #8 (Final Project Part 2)\n')
canvasX = 300
canvasY = 400
enemyChance = 2
enemies = [] #list of enemies
bullets = []
enemyBullets = []
spaceshipImg = p5.loadImage("sprites/spaceship.jpg")
enemy0Img = p5.loadImage("sprites/enemy1.png")
enemy1Img = p5.loadImage("sprites/enemy0.png")
bulletImg = p5.loadImage("sprites/bullet.png")
enemyBulletImg = p5.loadImage("sprites/bulletEnemy.png")


def setup():
  #called once
  p5.createCanvas(canvasX, canvasY)
  global player
  player = Spaceship(10, 150, 230, spaceshipImg)

  #spawn one enemy at the beginning
  enemies.append(Enemy(50, 50, enemy0Img))

def draw():
  #called continuously after setup()
  p5.background(51)  
  p5.fill(0)

  player.draw()

  spawn = random.randint(0, 1000)
  if spawn <= enemyChance:
    #spawn an enemy and add it to the list
    ex = random.randint(0, 280)
    ey = random.randint(0, 200)
    eimg = random.random()
    eimg = enemy1Img if eimg else enemy0Img
    enemies.append(Enemy(ex, ey, eimg))

  #draw the enemies
  for ele in enemies:
    ele.draw()
    ele.move()

  for bul in bullets:
    bul.draw()
    bul.move()
    
  for bul in enemyBullets:
    bul.draw()
    bul.move()
    #move
'''
Game logic
0.05 chance to generate an enemy each second
if enemy is hit remove from list
'''
# event functions below should be included,
# even if they don't do anything:

def keyPressed(event):
  #print('keyPressed.. ' + str(p5.key))
  #a/d: left to right movement
  if p5.key == 'a':
    #move to the left
    player.x -= 10
  elif p5.key == 'd':
    player.x += 10

def keyReleased(event):
  #print('keyReleased.. ' + str(p5.key))
  pass

def mousePressed(event):
  #print('mousePressed..')
  #this will control firing from the spaceship
  #right key for a missile?
  bullets.append(SelfBullet(player.x, player.y, bulletImg))
  pass

def mouseReleased(event):
  #print('mouseReleased..')
  pass

setup()
draw()
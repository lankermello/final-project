import js as p5
from classes import *
from movement import *
import random

print('Assignment #8 (Final Project Part 2)\n')
canvasX = 300
canvasY = 700
enemyChance = 5
enemies = [] #list of enemies
spaceshipImg = p5.loadImage("sprites/spaceship.jpg")
enemy0Img = p5.loadImage("sprites/enemy1.png")
enemy1Img = p5.loadImage("sprites/enemy0.png")


def setup():
  #called once
  p5.createCanvas(canvasX, canvasY)
  global player
  player = Spaceship(10, 150, 230, spaceshipImg)

def draw():
  #called continuously after setup()
  p5.background(255)  
  p5.fill(0)

  player.draw()

  spawn = random.randint(0, 100)
  if spawn <= enemyChance:
    pass
    #spawn an enemy and add it to the list
    
  

  
  
  
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
  if key == 'a':
    #move to the left
    spaceship.x -= 10
  elif key == 'd':
    spaceship.x += 10

def keyReleased(event):
  #print('keyReleased.. ' + str(p5.key))
  pass

def mousePressed(event):
  #print('mousePressed..')
  #this will control firing from the spaceship
  #right key for a missile?
  pass

def mouseReleased(event):
  #print('mouseReleased..')
  pass

setup()
draw()
  

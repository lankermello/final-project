import js as p5

print('Assignment #8 (Final Project Part 2)\n')
canvasX = 300
canvasY = 300
def setup():
  p5.createCanvas(canvasX, canvasY) 

def draw():
  p5.background(255)  
  p5.fill(0)
  

# event functions below should be included,
# even if they don't do anything:

def keyPressed(event):
  #print('keyPressed.. ' + str(p5.key))
  #a/d: left to right movement
  #space: dash
  pass

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
  

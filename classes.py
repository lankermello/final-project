import js as p5

bullMove = 5

class Spaceship:
  def __init__(self, hp, x, y, img):
    self.hp = hp
    self.x = x
    self.y = y
    self.img = img

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, 20, 40)
    p5.pop()

class Enemy:
  def __init__(self, x, y, img):

    self.x = x
    self.y = y
    self.img = img
    self.timer = 0
    
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, 10, 10)
    p5.pop()

  def move(self):
    self.timer += 1
    if self.timer == 40: self.timer = 0
    if self.timer < 20:
      self.x += 1
    else: self.x -= 1
    
  #function to fire
  #function to die and delete

class SelfBullet:
  def __init__(self, x, y, img):
    self.x = x
    self.y = y
    self.img = img

  def move(self):
    self.y -= bullMove

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, 2, 2)
    p5.pop()
  
    
class EnemyBullet:
  def __init__(self, x, y, img):
    self.x = x
    self.y = y
    self.img = img

  def move(self):
    self.y += bullMove

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, 5, 5)
    p5.pop()
'''
TODO
1. implement hitboxes
2. start menu
3. implement deletion of bullet and enemy
4. implement hit points
5. done???
'''
import js as p5

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
    
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, 10, 10)
    p5.pop()
  #function to fire
  #function to die and delete

class SelfBullet:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
class EnemyBullet:
  def __init__(self, x, y, damage):
    self.x = x
    self.y = y
    self. damage = damage
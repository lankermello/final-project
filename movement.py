def move_spaceship(x, y):
  #no wraparound


def hitbox(bulletx, bullety, targetx0, targetx1, targety0, targety1):
  #hit box calcs
  return (bulletx > targetx0 and bullet x < targetx1 and bullety < targety0 and bullety > targety1)
def hitbox(bulletx, bullety, targetx0, targetx1, targety0, targety1):
  return ((bulletx > targetx0) and (bulletx < targetx1) and (bullety > targety0) and (bullety < targety1))
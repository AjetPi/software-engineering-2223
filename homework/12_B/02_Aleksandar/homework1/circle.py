from enum import Enum
from math import sqrt

class Intersection(Enum):
    TOUCHING = 1
    NOTTOUCHING = 2
    INTERSECT = 3
    SAME = 4
    INSIDE = 5
    INVALID = 6

class Circle:
  def __init__(self, x, y,radius):
    self.x = x 
    self.y = y
    self.radius = radius

  def check(self,other):    
    dist = sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    if self.radius <= 0 or other.radius <= 0:
        return Intersection.INVALID.name 
    if self.x == other.x and self.y == other.y and self.radius == other.radius:
        return Intersection.SAME.name 
    elif (dist <= (self.radius - other.radius) or dist <= (other.radius - self.radius)):
        return Intersection.INSIDE.name 
    elif dist == (self.radius + other.radius):
        return Intersection.TOUCHING.name 
    elif dist < (self.radius + other.radius):
        return Intersection.INTERSECT.name 
    else:
        return Intersection.NOTTOUCHING.name 

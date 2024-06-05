import pygame as pg
from random import randint

vec2 = pg.math.Vector2


#GLOBALS VARIABLES THAT I USE IN GAME...
SCREEN = vec2(100, 100)

def generate_location_screen() -> vec2:
  return vec2(randint(0, SCREEN.x), randint(0, SCREEN.y))
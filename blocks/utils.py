import pygame as pg
from random import randint

vec2 = pg.math.Vector2


#GLOBALS VARIABLES THAT I USE IN GAME...
SCREEN = vec2(100, 100)

def generate_location_screen() -> vec2:
  return vec2(randint(0, SCREEN.x), randint(0, SCREEN.y))

def generate_position_out_of_screen() -> vec2:
    from random import choice
    x_offset = [-1, -4, -10, SCREEN.x + 1, SCREEN.x + 4, SCREEN.x + 10]
    y_offset = [-1, -4, -10, SCREEN.y + 1, SCREEN.y + 4, SCREEN.y + 10]

    x = choice(x_offset)
    y = choice(y_offset)

    return pg.math.Vector2(x, y)


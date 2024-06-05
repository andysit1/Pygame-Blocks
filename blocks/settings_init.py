import os
import pygame as pg

BASE = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sprites_frame_size = (60, 60)

#Note: must start at sprite_name_frame at 1...
def load_sprites_from_folder(filename : str) -> list:
  sprite_sheet = []
  c = 0
  running = True
  while running:
    seaweed_frame_path =  os.path.join(BASE, filename, "seaweed{}.png".format(str(c + 1)))
    c += 1

    try:
      frame = pg.image.load(seaweed_frame_path)
      sprite_sheet.append(pg.transform.scale(frame, sprites_frame_size))
    except:
      running = False

  return sprite_sheet





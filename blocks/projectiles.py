import pygame as pg
from utils import generate_location_screen
from random import randint
vec2 = pg.math.Vector2

#just for the sake for the example here.
filler_sprite_projectile = pg.Surface()


#Project class to handle creating shots objects..
  #Notes:
    #When implementing need to write a way to vary speed and sizing better..
class Projectiles(pg.sprite.Sprite):
  def __init__(self, groups):
    super().__init__(groups)

    self.image = pg.transform.scale(filler_sprite_projectile.convert_alpha(), (32, 32))

    self.rect = self.image.get_rect()
    self.rect.x, self.rect.y = generate_location_screen()

    #respawn timer to delay
    self.respawn_timer = .2
    self.shots = []


  def create_shot(self):
    speed = randint(20, 45)
    return {
            'surface' :  filler_sprite_projectile,
            'position' : pg.Vector2(self.rect.x,  self.rect.y),
            'speed' : speed,
            'direction' : pg.Vector2(0, -1),
            'radius' : 7,
            'life' : 0.5
          }

    #handles remove and update
  def update_shot(self, dt):
    for shot in self.shots:
      shot['position'] += shot['direction'] * shot['speed'] * dt
      shot['life'] -= 1 * dt

      if shot['life'] < 0:
        try:
          self.shots.remove(shot)
        except:
          pass

  def draw_shot(self, surface: pg.Surface):
    for shot in self.shots:
      if shot:
        surface.blit(shot['surface'].convert_alpha(), shot['position'])

  def update(self, dt):
    self.update_shot(dt)

    self.respawn_timer -= 1 * dt
    if self.respawn_timer < 0:
      for _ in range(3):
        self.shots.append(self.create_shot())
      self.respawn_timer = .2
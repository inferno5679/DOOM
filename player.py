from settings import *
import pygame as pg
import math

class Player:
    def __init__(self,game):
        self.game = game
        self.x, self.y = player_pos
        self.angle = player_angle
        self.shot = False
        self.diag_move_corr = 1 / math.sqrt(2)
        self.health = player_max_health
        self.rel = 0


    def calculate_rel(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5  
    def check_game_over(self):
        if self.health < 1:
            if self.game.sound.player_death is None:
                print("Debug: player_death sound is not initialized")
                return
            self.game.sound.player_death.play()
            self.game.object_renderer.game_over()
            pg.display.flip
            pg.time.delay(1500)
            self.game.new_game()
    
    def get_damage(self,damage):
        self.health -= damage
        self.game.object_renderer.player_damage()
        self.game.sound.player_pain.play()
        self.check_game_over()

    def single_fire_event(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True

    
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = player_speed * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        num_key_pressed = -1
        if keys[pg.K_w]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            num_key_pressed += 1
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            num_key_pressed += 1
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            num_key_pressed += 1
            dx += -speed_sin
            dy += speed_cos
        if keys[pg.K_w] and keys[pg.K_LSHIFT]:
            num_key_pressed += 1
            dx += speed_cos*2
            dy += speed_sin*2

        # diag move correction
        if num_key_pressed:
            dx *= self.diag_move_corr
            dy *= self.diag_move_corr

        self.check_wall_collision(dx, dy)

        # if keys[pg.K_LEFT]:
        #     self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        # if keys[pg.K_RIGHT]:
        #     self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = player_size_scale / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                    (self.x * 100 + width * math.cos(self.angle),
                        self.y * 100 + width * math. sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < mouse_border_left or mx > mouse_border_right:
            pg.mouse.set_pos([half_width, half_height])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-mouse_max_rel, min(mouse_max_rel, self.rel))
        self.angle += self.rel * mouse_sensitivity * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('game_dev/resources/textures/sky.png',(width,half_height))
        self.sky_offset = 0
        self.blood_screen = self.get_texture("game_dev/resources/textures/blood_screen.png",Res)
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'game_dev/resources/textures/digits/{i}.png',[self.digit_size]*2)
                             for i in range(11)]
        self.digits = dict(zip(map(str,range(11)),self.digit_images))
        self.game_over_image = self.get_texture("game_dev/resources/textures/game_over.png",Res)
    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()

    def game_over(self):
        self.screen.blit(self.game_over_image,(0,0))

    def draw_player_health(self):
        health = str(self.game.player.health)
        for i,char in enumerate(health):
            self.screen.blit(self.digits[char],(i*self.digit_size,0))
        self.screen.blit(self.digits['10'],((i+1) * self.digit_size,0))

    def player_damage(self):
        self.screen.blit(self.blood_screen,(0,0))
    
    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.0 * self.game.player.rel) % width
        self.screen.blit(self.sky_image, (-self.sky_offset,0))
        self.screen.blit(self.sky_image,(-self.sky_offset + width,0))
        #floor
        pg.draw.rect(self.screen,floor_colour,(0,half_height,width,height))
    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render,key = lambda t: t[0],reverse=True)
        for depth,image, pos in list_objects:
            self.screen.blit(image,pos)


    @staticmethod
    def get_texture(path, res=(texture_size, texture_size)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('game_dev/resources/textures/out.png'),
            2: self.get_texture('game_dev/resources/textures/out2.png'),
            3: self.get_texture('game_dev/resources/textures/out3.png'),
            4: self.get_texture('game_dev/resources/textures/out4.png'),
            5: self.get_texture('game_dev/resources/textures/out5.png'),
        }
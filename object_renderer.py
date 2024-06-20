import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('game_dev/resources/textures/sky.png',(width,half_height))
        self.sky_offset = 0
    
    def draw(self):
        self.draw_background()
        self.render_game_objects()
    
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
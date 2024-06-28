from sprite_object import *
from npc import *

class objectHandler:
    def __init__(self,game) -> None:
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = "game_dev/resources/sprites/npc"
        self.static_sprite_path = 'game_dev/resources/sprites/static_sprites/candlebra.png'
        self.animated_sprite_path = 'game_dev/resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positons={}

        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game,pos=(11.5,14.5)))
        add_sprite(AnimatedSprite(game,path= self.animated_sprite_path + 'red_light/0.png',pos=(14.5,5.5)))
        add_sprite(AnimatedSprite(game,path= self.animated_sprite_path + 'red_light/0.png',pos=(14.5,11.5)))

        #npc map
        add_npc(NPC(game))
        add_npc(NPC(game),pos=(11.5,4.5))

    def update(self):
        self.npc_positons = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_sprite(self,sprite):
        self.sprite_list.append(sprite)

    def add_npc(self,npc):
        self.npc_list.append(npc)
import pygame as pg

class Sound():
    def __init__(self,game):
        self.game = game
        pg.mixer.init()
        self.path="game_dev/resources/sound/"
        self.shotgun= pg.mixer.Sound(self.path + "doom_shotgun_firing_sound_effect.wav")
        self.npc_pain = pg.mixer.Sound(self.path + "dspopain.wav")
        self.npc_death = pg.mixer.Sound(self.path + "dspodth1.wav")
        self.npc_shot = pg.mixer.Sound(self.path + "npc_attack.wav")
        self.player_pain = pg.mixer.Sound(self.path + "player_pain.wav")
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
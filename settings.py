import math
# Game settigs

Res = width,height = 1600,900
half_width = width//2
half_height = height//2
Fps = 60
player_size_scale = 60

player_pos = 1.5,5 # mini_map
player_angle = 0
player_speed = 0.004
player_rotation_speed = 0.002
player_max_health = 100

mouse_sensitivity = 0.0003
mouse_max_rel=40
mouse_border_left = 100
mouse_border_right = width - mouse_border_left

floor_colour = (30,30,30)

FOV = math.pi / 3

half_fov = FOV/2
num_rays = width//2
half_num_rays = num_rays//2
delta_angle = FOV/num_rays
max_depth = 20

screen_dist = half_width / math.tan(half_fov)
scale = width//num_rays

texture_size = 256
half_texture = texture_size//2
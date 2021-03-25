import os
import pygame


# Asset folders
game_folder = os.path.dirname(__file__)
maps_folder = os.path.join(game_folder, 'maps')


# Map
# Read .txt file from 'maps' folder and interprets it
map_1 = os.path.join(maps_folder, 'test_map_1.txt')
map_file = open(map_1, 'r')
lines = map_file.readlines()
x_map = []
xy_map = []

for element in lines:
    x_map = []
    for i in element:
        if i not in [' ', '\n']:
            x_map.append(i)
    xy_map.append(x_map)


print(xy_map)
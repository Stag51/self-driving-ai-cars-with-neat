# Author: Saad Shabbir
# Developed at HeadQuarters at S.T.A.G LLc.

# Importing all the libraries
import math
import random
import os
import sys

import neat
import pygame

WIDTH = 1920
HEIGHT = 1080

CAR_SIZE_X = 60
CAR_SIZE_Y = 60

# Color to crash on hit
BORDER_COLOR = (255, 255, 255, 255) 


# Generation Counter
current_generation = 0

class Car:

    def __init__(self):
        # Loading car Sprite and Rotation
        # Convert Speeds up the car A lot
        self.sprite = pygame.image.load('car.png').convert()
        self.sprite = pygame.transform.scale(self.sprite, (CAR_SIZE_X, CAR_SIZE_Y))
        self.rotate_sprite = self.sprite

        # Starting position

        self.position = [830, 920]
        self.angle = 0
        self.speed = 0

        # Flag for default speed later on
        self.center = [self.position[0] + CAR_SIZE_X/2, self.position[1] + CAR_SIZE_Y/2] # Calculating the center

        # List For Sensors and Radars
        self.radars = []
        # Radars to be drawn
        self.drawing_radars = []

        # Boolen to check if car is crashed or not
        self.alive = True
        
        # Distance Driven
        self.distance = 0
        # Time Passed
        self.time = 0

    def draw(self, screen):
        # Drawing Sprite
        screen.blit(self.rotate_sprite, self.position)]
        # Drawing Radars which is optional as of I see
        self.draw_radars(screen)

    def draw_radar(self, screen):
        # Optional for radars
        for radar in self.radars:
            position = radar[0]
            pygame.dr
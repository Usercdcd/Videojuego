import os

import pygame

from src.settings import Settings


def play():
    soundtrack = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'audio', 'Noisia_dustup.mp3'))
    soundtrack.play(loops=-1)
    soundtrack.set_volume(Settings.SOUNDTRACK_VOLUME)

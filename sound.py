import pygame
import threading

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()

    def play_effect(self, file):
        sound = pygame.mixer.Sound(file)
        sound.play()

    def play_music(self, file, volume=0.2):
        pygame.mixer.music.load(file)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()


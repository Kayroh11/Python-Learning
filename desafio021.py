import pygame

pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()
input()
pygame.event.wait()

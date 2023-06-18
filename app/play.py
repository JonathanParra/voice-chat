
import pygame



pygame.init()
pygame.mixer.init()

#carga archivo mp3.
pygame.mixer.music.load("mp3/voice.mp3")

pygame.mixer.music.play()

#espera a que se complete la reproducción del audio.
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

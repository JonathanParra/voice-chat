from gtts import gTTS
import pygame

text = "Hola Jonathan, buenos días. como estas?"

tts = gTTS(text)
tts.save("mp3/voice.mp3")
tts = gTTS(text, lang="es", slow=True)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("mp3/voice.mp3")
pygame.mixer.music.play()

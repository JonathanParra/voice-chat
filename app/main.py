from gtts import gTTS
import pygame

text = "Hola Jonathan, buenos días. como estas?"

tts = gTTS(text)
tts.save("hola.mp3")
tts = gTTS(text, lang="es", slow=True)

'''pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("hola.mp3")
pygame.mixer.music.play()
'''
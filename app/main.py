from gtts import gTTS
import pygame

#modulo que carga el texto
text = "Hola, buenas tardes. Escribe en este campo lo que quieres que reproduzca"
tts = gTTS(text)
tts.save("mp3/voice.mp3")
tts = gTTS(text, lang="es", slow=True)


#modulo que reproduce el mp3
pygame.init()
pygame.mixer.init()

#carga archivo mp3.
pygame.mixer.music.load("mp3/voice.mp3")

pygame.mixer.music.play()

#espera a que se complete la reproducción del audio.
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


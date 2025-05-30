import pyaudio
import wave
import subprocess
import openai
from gtts import gTTS
import pygame
import os
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENIA-KEY") 
nombre_archivo = "mp3/audio.wav"
duracion_grabacion = 10  # duración en segundos


def grabar_audio(nombre_archivo, duracion):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    print("Grabando audio...")

    for i in range(0, int(RATE / CHUNK * duracion)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finalizada la grabación.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(nombre_archivo, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def whisper():
    # Ejecuta el comando y guarda la salida en una variable
    comando = "whisper mp3/audio.wav --language Spanish"
    resultado = subprocess.check_output(comando, shell=True)
    return resultado


def convert_audio_a_text(resultado):
    # Convierte el resultado en una cadena de texto decodificada
    resultado_decodificado = resultado.decode("utf-8")

    # Imprime el resultado
    print(resultado_decodificado)
    return resultado_decodificado


def motor_gpt(resultado_decodificado):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Modelo de lenguaje a utilizar (GPT-3)
        prompt=resultado_decodificado,
        max_tokens=100,  # Número máximo de tokens en la respuesta generada
        temperature=0.7,  # Controla la aleatoriedad de las respuestas generadas (0.2 - 1.0)
        n=1,  # Número de respuestas a generar
        stop=None,  # Puedes especificar una cadena de texto para detener la generación
    )

    respuesta_generada = response.choices[0].text.strip()
    print(respuesta_generada)
    return respuesta_generada


def resp_generada(respuesta_generada):
    # modulo que carga el texto
    text = respuesta_generada
    tts = gTTS(text)
    tts.save("mp3/voice.mp3")
    tts = gTTS(text, lang="es", slow=True)


def reproduce_audio():
    # modulo que reproduce el mp3
    pygame.init()
    pygame.mixer.init()

    # carga archivo mp3.
    pygame.mixer.music.load("mp3/voice.mp3")

    pygame.mixer.music.play()

    # espera a que se complete la reproducción del audio.
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


grabar_audio(nombre_archivo, duracion_grabacion)
resultado = whisper()
resultado_decodificado = convert_audio_a_text(resultado)
respuesta_generada = motor_gpt(resultado_decodificado)
resp_generada(respuesta_generada)
reproduce_audio()

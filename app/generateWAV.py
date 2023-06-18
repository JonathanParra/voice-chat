import pyaudio
import wave

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

# Ejemplo de uso
nombre_archivo = "mp3/audio.wav"
duracion_grabacion = 5  # duración en segundos

grabar_audio(nombre_archivo, duracion_grabacion)



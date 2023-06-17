import subprocess

# Ejecuta el comando y guarda la salida en una variable
comando = "whisper mp3/voice.mp3 --language Spanish"
resultado = subprocess.check_output(comando, shell=True)

# Convierte el resultado en una cadena de texto decodificada
resultado_decodificado = resultado.decode("utf-8")

# Imprime el resultado
print(resultado_decodificado)


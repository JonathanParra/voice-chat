# voice-chat


```
whisper japanese.wav --language Japanese
```


# Opciones para TTS y STT

  
## Usando APIs de Servicios en la Nube

#### Google Cloud (Text-to-Speech y Speech-to-Text)


+ Text-to-Speech (TTS): Ofrece voces altamente naturales (Neural2) e incluso "voces de estudio" y "Chirp 3" para diálogos conversacionales, con entonaciones precisas y vacilaciones humanas. Soporta SSML para un control fino de la pronunciación, pausas, etc. Es conocido por su baja latencia.

+ Speech-to-Text (STT): Proporciona transcripciones precisas en tiempo real o para audio pregrabado. Ideal para una amplia gama de aplicaciones.

#### Amazon Web Services (AWS)

+ Amazon Polly (TTS): Permite convertir texto en voz realista. Ofrece una amplia selección de voces y estilos, incluyendo voces "neuronales" que suenan muy naturales. Es muy eficiente para grandes volúmenes de texto.

+ Amazon Transcribe (STT): Transcribe audio a texto de forma precisa. Ofrece capacidades de transcripción en tiempo real y por lotes, identificación de locutores y compatibilidad con varios idiomas.


#### Microsoft Azure

+ Azure Text-to-Speech (TTS): Ofrece voces neuronales de alta calidad que suenan muy naturales. Permite la personalización de voces y control de audio en más de 110 voces y 45 idiomas. Es flexible en opciones de despliegue (nube, local, edge).

+ Azure Speech-to-Text (STT): Reconocimiento de voz altamente preciso con opciones de personalización para diferentes dominios.

#### IBM Watson

+ IBM Watson Text to Speech (TTS): Servicio API basado en la nube que convierte texto en audio natural en varios idiomas.

+ IBM Watson Speech to Text (STT): Reconocimiento de voz con opciones de entrenamiento de modelos para mejorar la precisión y transcripción de baja latencia para aplicaciones en tiempo real.

#### OpenAI (Whisper para STT, y tienen sus propias APIs de TTS)

+ Whisper (STT): Es un modelo de código abierto muy aclamado de OpenAI por sus capacidades de voz a texto y traducción. Es extremadamente preciso y soporta una gran cantidad de idiomas. Puedes usar su API o ejecutarlo localmente (más avanzado).

+ OpenAI TTS API: Ofrecen su propio servicio de Text-to-Speech con voces de IA generativa.


#### Otros proveedores y APIs destacadas:

+ ElevenLabs (TTS): Conocida por sus voces de IA extremadamente realistas y la capacidad de clonar voces.

+ PlayHT (TTS): Se destaca por su muy baja latencia (menos de 300 ms), ideal para IA conversacionales en tiempo real.

+ Deepgram (STT y TTS): Ofrecen un STT muy preciso y de baja latencia, y recientemente han lanzado Deepgram Aura (TTS) enfocada en agentes de IA conversacionales con ultra baja latencia.

+ Murf.ai (TTS): Popular para creadores de contenido, ofrece más de 120 voces en 20 idiomas.

+ Speaktor (TTS): Soporta más de 50 idiomas y se enfoca en alta precisión y eficiencia.


## Usando Soluciones de Código Abierto (Open Source)

### Para Voz a Texto (STT):

+ OpenAI Whisper: Como mencioné, es un modelo de código abierto muy potente y preciso. Puedes ejecutarlo localmente (requiere hardware decente, especialmente para modelos más grandes) o a través de su API. Hay implementaciones optimizadas como Faster Whisper y Distil-Whisper para mayor velocidad.

+ Vosk: Una solución de reconocimiento de voz offline, ligero y de código abierto. Soporta múltiples idiomas. Bueno para dispositivos con recursos limitados.

+ Coqui STT: Otro proyecto de código abierto para STT.

+ SpeechBrain: Una biblioteca de código abierto para diversas tareas de voz, incluyendo STT.

### Para Texto a Voz (TTS):

+ Coqui TTS (XTTS v2): Una de las opciones de código abierto más populares para TTS, con voces que suenan naturales y soporte para clonación de voz a partir de una muestra.

+ Piper: Un sintetizador de voz ligero y rápido, ideal para ejecución en dispositivos.

+ MaryTTS: Una arquitectura modular y flexible para construir sistemas TTS, que permite crear voces nuevas a partir de audio grabado.

+ eSpeak: Un sintetizador de voz compacto, conocido por su sencillez y bajo consumo de recursos, aunque las voces pueden sonar más robóticas.

+ Tortoise TTS: Otro modelo de TTS de código abierto que ha ganado popularidad.

+ Kokoro: Un modelo TTS open-source muy pequeño (82M parámetros) que es rápido y económico de ejecutar, incluso en CPU. Ideal para aplicaciones en tiempo real.

+ Fish Speech v1.5: Afirma una latencia de menos de 150 ms, y soporta múltiples idiomas.

### ¿Cómo integrar una solución de código abierto?

+ Instalación: Descarga e instala las librerías y modelos necesarios (generalmente a través de pip para Python).

+ Carga el modelo: Carga el modelo pre-entrenado en memoria.

+ #### Procesamiento:
    + Para STT: Pasa el audio al modelo para obtener el texto.
    + Para TTS: Pasa el texto al modelo para generar el audio.
 
+ Manejo de recursos: Deberás gestionar el uso de CPU/GPU y memoria.


# Precios de APIs de Voz a Texto (STT) y Texto a Voz (TTS) en la Nube (Mayo 2025)

**Nota Importante:** Los precios son **aproximados** y pueden variar. Consulta siempre la **página oficial de precios** del proveedor para la información más actualizada. La mayoría ofrece un **nivel gratuito** para probar.

| Proveedor / Servicio | Funcionalidad | Nivel Gratuito (Ejemplo) | Precio Estándar (aprox.) | Notas Clave |
| :------------------- | :------------ | :----------------------- | :----------------------- | :---------- |
| **Google Cloud** | **TTS** | 250k caracteres/mes (Neural) | **$16 / 1M caracteres** (Neural) | Varía por tipo de voz (Standard/Neural) y volumen. |
|                      | **STT** | 60 minutos/mes           | **$0.024 / minuto** | Varía por audio (estándar, telefónico) y si es en tiempo real. |
| **Amazon Web Services (AWS)** | **TTS (Polly)** | 5M caracteres/mes (Standard) <br> 1M caracteres/mes (Neural) | **$4 / 1M caracteres** (Standard) <br> **$16 / 1M caracteres** (Neural) | Voces Standard vs. Neural con diferentes precios. |
|                      | **STT (Transcribe)** | 60 minutos/mes           | **$0.024 / minuto** | Varía por región, tiempo real y características avanzadas. |
| **Microsoft Azure** | **TTS** | 500k caracteres/mes (Neural) | **$16 / 1M caracteres** (Neural) | Precios diferentes para voces estándar, neuronales y personalizadas. |
|                      | **STT** | 5 horas/mes              | **$1 / hora** | Varía por tipo de reconocimiento y tiempo real. |
| **IBM Watson** | **TTS** | 10k caracteres/mes       | **$0.02 / 1k caracteres**| Precios por carácter. Ofrece voces estándar y neuronales. |
|                      | **STT** | 500 minutos/mes          | **$0.02 / minuto** | Precios por minuto. Diferentes modelos (telefónico, banda ancha). |
| **OpenAI** | **TTS API** | No hay específico          | **$0.015 / 1k caracteres** | Precio único por caracteres procesados. |
|                      | **Whisper API (STT)** | No hay específico          | **$0.006 / minuto** | Altamente preciso. |
| **ElevenLabs** | **TTS** | 10k caracteres/mes       | **Desde $5/mes** (30k caracteres) | Planes de suscripción con diferentes volúmenes y funciones (clonación de voz). |
| **PlayHT** | **TTS** | Nivel gratuito (limitado) | **Desde $31.2/mes** (600k caracteres, pago anual) | Planes de suscripción. Conocido por baja latencia. |
| **Deepgram** | **Aura (TTS)**| 500k caracteres/mes (Dev) | **Contactar Ventas** | Enfocado en IA conversacionales de ultra baja latencia. |
|                      | **STT** | $200 de crédito          | **$0.015 - $0.045 / minuto** | Varía por modelo y funciones avanzadas (diarización). |
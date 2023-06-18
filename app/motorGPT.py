import openai

openai.api_key = 'TU_CLAVE_DE_API'


response = openai.Completion.create(
    engine='text-davinci-003',  # Modelo de lenguaje a utilizar (GPT-3)
    prompt='Tu texto de entrada aquí',
    max_tokens=100,  # Número máximo de tokens en la respuesta generada
    temperature=0.7,  # Controla la aleatoriedad de las respuestas generadas (0.2 - 1.0)
    n=1,  # Número de respuestas a generar
    stop=None,  # Puedes especificar una cadena de texto para detener la generación
)

respuesta_generada = response.choices[0].text.strip()
print(respuesta_generada)


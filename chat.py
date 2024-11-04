import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno desde .env
openai.api_key = os.getenv("OPENAI_API_KEY")

def obtener_respuesta(mensaje):
    respuesta = openai.ChatCompletion.create(
        model="gpt-4",  # O el modelo que elijas
        messages=[{"role": "user", "content": mensaje}]
    )
    return respuesta.choices[0].message["content"]

# Bucle simple para interactuar
while True:
    mensaje = input("Tú: ")
    if mensaje.lower() == "salir":
        break
    print("Chatbot:", obtener_respuesta(mensaje))

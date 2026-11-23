
import os

from dotenv import load_dotenv
from google import genai


# Cargar las variables del archivo .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL")

if not api_key or not model:
    raise ValueError(
        "Falta configurar GEMINI_API_KEY o GEMINI_MODEL en .env"
    )


def main():
    try:
        # Crear cliente de Gemini
        client = genai.Client(api_key=api_key)

        # Enviar una solicitud real al modelo
        response = client.models.generate_content(
            model=model,
            contents="Responde únicamente con el texto: CONEXION_EXITOSA"
        )

        print("Conexión con Gemini establecida correctamente.")
        print("Modelo utilizado:", model)
        print("Respuesta del modelo:", response.text)

    except Exception as error:
        print("No se pudo establecer la conexión con Gemini.")
        print("Tipo de error:", type(error).__name__)
        print("Detalle:", str(error))


if __name__ == "__main__":
    main()

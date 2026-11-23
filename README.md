# AI Support Engine

## Descripción del proyecto

AI Support Engine es un prototipo de clasificación inteligente de solicitudes de soporte técnico que utiliza dos motores de análisis:

- **Motor tradicional:** utiliza reglas y palabras clave para identificar categorías y prioridades.
- **Motor generativo:** utiliza Google Gemini para analizar mensajes, clasificarlos y generar respuestas contextualizadas.

El sistema permite identificar problemas de acceso, errores del sistema, solicitudes de nuevas funcionalidades e incidentes de seguridad.

Elaborado por: Juan Carlos Victoria García

## Objetivos

- Clasificar solicitudes de soporte técnico.
- Asignar niveles de prioridad.
- Generar respuestas para los usuarios.
- Identificar incidentes que requieren revisión humana.
- Comparar el funcionamiento de un motor tradicional y uno generativo.

## Tecnologías utilizadas

- Python 3.14
- FastAPI
- Google Gemini API
- Pydantic
- Uvicorn
- Pytest
- HTTPX
- python-dotenv

## Categorías de clasificación

| Categoría | Descripción |
|---|---|
| ACCESS | Problemas relacionados con el acceso a cuentas y sistemas. |
| BUG | Errores o fallas en el funcionamiento de la aplicación. |
| FEATURE | Solicitudes de nuevas funcionalidades o mejoras. |
| SECURITY | Incidentes o posibles amenazas de seguridad. |

## Niveles de prioridad

| Prioridad | Descripción |
|---|---|
| LOW | Solicitudes de bajo impacto. |
| MEDIUM | Problemas que afectan parcialmente al usuario. |
| HIGH | Problemas importantes que afectan las operaciones. |
| CRITICAL | Incidentes graves que requieren atención prioritaria. |

## Requisitos previos

- Python 3.14 o compatible.
- Git.
- Una clave de Google Gemini API para utilizar el motor generativo.

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone URL_DEL_REPOSITORIO
   ```

2. Entrar en la carpeta del proyecto:

   ```bash
   cd AI-Support-Engine
   ```

3. Crear un entorno virtual:

   ```powershell
   python -m venv .venv
   ```

4. Activar el entorno virtual en Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Instalar las dependencias:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Configuración de variables de entorno

Crear un archivo `.env` en la raíz del proyecto utilizando `.env.example` como referencia.

Configurar las siguientes variables:

```env
GEMINI_API_KEY=TU_CLAVE_DE_API
GEMINI_MODEL=gemini-3.5-flash-lite
```

**Importante:** No compartir ni subir el archivo `.env` a GitHub. La clave de API debe mantenerse privada.

## Ejecución del proyecto

Iniciar el servidor con:

```bash
python -m uvicorn app.presentation.api:app --reload
```

La API estará disponible en:

`http://127.0.0.1:8000`

La documentación interactiva de Swagger estará disponible en:

`http://127.0.0.1:8000/docs`

## Endpoint principal

### POST /api/analyze

Permite analizar una solicitud de soporte técnico.

Ejemplo de solicitud:

```json
{
  "message": "No puedo iniciar sesión en mi cuenta",
  "mode": "generative"
}
```

El campo `mode` permite seleccionar:

- `traditional`: utiliza el motor basado en reglas.
- `generative`: utiliza el motor de Google Gemini.

Ejemplo de respuesta:

```json
{
  "category": "ACCESS",
  "priority": "MEDIUM",
  "response": "El problema está relacionado con el acceso a su cuenta...",
  "requiresHumanReview": false,
  "mode": "generative"
}
```

## Pruebas

Para ejecutar las pruebas automatizadas:

```bash
python -m pytest -v
```

Las pruebas verifican el funcionamiento de los motores, la normalización de mensajes y la detección local de posibles incidentes de seguridad.

También se realizaron pruebas manuales mediante Swagger para evaluar ambos motores, las solicitudes ambiguas, los incidentes de seguridad y los intentos de Prompt Injection.

## Seguridad

- Las claves de API se almacenan en variables de entorno.
- La API valida los mensajes y los modos permitidos.
- Los mensajes deben tener entre 1 y 5000 caracteres.
- Los incidentes clasificados como SECURITY requieren revisión humana.
- El motor generativo incorpora instrucciones para resistir intentos de manipulación mediante Prompt Injection.

La detección de incidentes de seguridad utiliza reglas locales complementarias y no sustituye una auditoría o un sistema de seguridad especializado.

## Estructura del proyecto

```text
AI-Support-Engine/
│
├── app/
│   ├── application/
│   │   └── schemas.py
│   ├── database/
│   ├── engines/
│   │   ├── base.py
│   │   ├── traditional.py
│   │   └── generative.py
│   ├── infrastructure/
│   ├── presentation/
│   │   └── api.py
│   └── security/
│
├── docs/
├── scripts/
├── tests/
│   ├── test_traditional.py
│   └── test_generative.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Resultados de evaluación

En las diez solicitudes evaluadas con el motor generativo se obtuvieron los siguientes resultados:

| Criterio | Resultado |
|---|---:|
| Clasificación de categorías | 100 % |
| Clasificación de prioridades | 45% % |
| Coincidencia conjunta | 85% % |

También se realizaron dos pruebas de Prompt Injection, en las cuales el motor identificó correctamente los incidentes de seguridad y solicitó revisión humana.

## Conclusión

AI Support Engine demuestra cómo combinar un motor tradicional basado en reglas con un motor generativo para automatizar la clasificación de solicitudes de soporte. Las pruebas permitieron comprobar la clasificación de categorías, asignación de prioridades, generación de respuestas y validación de entradas. Aunque los resultados fueron satisfactorios, existen oportunidades de mejora en la precisión de las prioridades y en los mecanismos de detección de incidentes de seguridad.
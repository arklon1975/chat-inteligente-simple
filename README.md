# Multimodal PDF Summarizer with LangChain & OpenAI

Este proyecto analiza documentos PDF que contienen texto, tablas e imágenes, extrayendo información de cada tipo de contenido, resumiéndola mediante modelos LLM de OpenAI, y almacenando los resúmenes en una base vectorial para su posterior recuperación.

## Características

- 📄 Extracción de texto y tablas de documentos PDF con `unstructured`.
- 🖼️ Extracción y análisis de imágenes embebidas con `pytesseract` y `gpt-4o`.
- 🧠 Resumen automático usando `gpt-3.5-turbo` y `gpt-4o`.
- 🔍 Almacenamiento de resúmenes en Chroma + InMemoryStore con `LangChain MultiVectorRetriever`.
- ❓ Interfaz de preguntas-respuestas multimodal sobre el contenido procesado.

## Requisitos

- Python 3.10 o superior
- API key de OpenAI (`OPENAI_API_KEY`)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) instalado localmente

## Instalación

1. Clona este repositorio.
2. Instala dependencias (recomendado usar entorno virtual con `Poetry` o `venv`):

```bash
pip install -r requirements.txt


Asegúrate de tener Tesseract instalado y la ruta correcta especificada en el script:

python
Copiar
Editar
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
Crea un archivo .env con tu clave de OpenAI:

env
Copiar
Editar
OPENAI_API_KEY=tu_clave_api
Uso
Coloca el archivo PDF que deseas analizar en la misma carpeta que el script y asegúrate de que se llame startupai-financial-report-v2.pdf.

Ejecuta el script:

bash
Copiar
Editar
python 001-multimodal.py
El script imprimirá los resúmenes de texto, tablas e imágenes y responderá preguntas sobre el contenido del PDF.

Uso
Coloca el archivo PDF que deseas analizar en la misma carpeta que el script y asegúrate de que se llame startupai-financial-report-v2.pdf.

Ejecuta el script:

bash
Copiar
Editar
python 001-multimodal.py
El script imprimirá los resúmenes de texto, tablas e imágenes y responderá preguntas sobre el contenido del PDF.

Estructura del Proyecto
bash
Copiar
Editar
.
├── 001-multimodal.py
├── .env
├── figures/                   # Carpeta generada con las imágenes extraídas
└── startupai-financial-report-v2.pdf
Preguntas de ejemplo que puedes hacer
¿Qué ves en las imágenes?

¿Cuál es el nombre de la empresa?

¿Qué producto se muestra en la imagen?

¿Cuáles son los gastos totales de la empresa?

¿Cuál es el ROI?

¿Cuánto vendió la empresa en 2023 y 2022?

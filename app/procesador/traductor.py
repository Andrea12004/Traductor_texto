
import os
import re
import unicodedata  # Para eliminar tildes

# Lista de identificadores de video
word_ids = [
    "como_estas",
    "hola",
    "gracias",
    "buenos_dias",
    "buenas_tardes",
    "buenas_noches",
    "A",
    "B"
]

# Carpeta de los videos
VIDEO_FOLDER = os.path.abspath("videos") 


def quitar_tildes(texto):
    """Elimina tildes y caracteres diacríticos de un texto."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def procesar_frase(frase):
    frase = frase.lower().strip()
    frase = quitar_tildes(frase)  # Eliminar tildes
    frase = re.sub(r"[^\w\s]", "", frase)  # Eliminar puntuación
    palabras = frase.split()
    i = 0
    secuencia_videos = []

    max_bloque = 10  

    while i < len(palabras):
        encontrado = False
        for n in range(max_bloque, 0, -1):
            if i + n <= len(palabras):
                bloque = "_".join(palabras[i:i+n])
                if bloque in word_ids:
                    secuencia_videos.append(bloque)
                    i += n
                    encontrado = True
                    break
        if not encontrado:
            i += 1

    return secuencia_videos
def obtener_rutas_videos(video_ids: list) -> list:
    rutas = []
    for vid in video_ids:
        rutas.append({
            "id": vid,
            "url": f"https://<tu-api>.onrender.com/video/{vid}"
        })
    return rutas
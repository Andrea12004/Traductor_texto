
from fastapi import FastAPI
from pydantic import BaseModel
from app.procesador.traductor import procesar_frase, obtener_rutas_videos

app = FastAPI()

class Frase(BaseModel):
    texto: str

@app.post("/procesar")
def procesar(frase: Frase):
    video_ids = procesar_frase(frase.texto)
    videos = obtener_rutas_videos(video_ids)
    return {"videos": videos}

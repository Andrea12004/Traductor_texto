from fastapi import FastAPI
from fastapi.responses import FileResponse 
from pydantic import BaseModel
import os 

from app.procesador.traductor import procesar_frase, obtener_rutas_videos

app = FastAPI()

class Frase(BaseModel):
    texto: str

@app.post("/procesar")
def procesar(frase: Frase):
    video_ids = procesar_frase(frase.texto)
    videos = obtener_rutas_videos(video_ids)
    return {"videos": videos}

@app.get("/video/{video_id}")
def get_video(video_id: str):
    video_path = os.path.join("videos", f"{video_id}.mp4")
    if not os.path.exists(video_path):
        return {"error": "Video no encontrado"}
    return FileResponse(video_path, media_type="video/mp4")


@app.get("/listar_videos")
def listar_videos():
    archivos = os.listdir("videos")
    return {"videos_disponibles": archivos}

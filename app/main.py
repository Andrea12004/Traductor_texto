from fastapi.responses import FileResponse
import os

@app.get("/video/{video_id}")
def get_video(video_id: str):
    video_path = os.path.join("videos", f"{video_id}.mp4")
    if not os.path.exists(video_path):
        return {"error": "Video no encontrado"}
    return FileResponse(video_path, media_type="video/mp4")

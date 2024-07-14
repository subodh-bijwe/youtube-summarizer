import threading
from src.generate_from_ollama import get_summary
from src.generate_transcription import get_transcription
from src.video_name import get_video_title_from_link, extract_video_id
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
app = FastAPI()


@app.get('/')
def hc():
    return {"message": "Transcription service is up and running!"}

@app.post('/summarize')
async def summarize(request: Request):
    body =  await request.json()
    y_link = body["link"]
    video_id = extract_video_id(y_link)
    fname = get_video_title_from_link(video_id)
    transcription = get_transcription(video_id)
    thread1 = threading.Thread(target=get_summary, args=(transcription,fname))
    thread1.start()
    return JSONResponse({
        "message": f"Summary will be saved in {fname}.md file in summaries folder."
        })
                
    
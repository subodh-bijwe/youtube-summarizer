from youtube_transcript_api import YouTubeTranscriptApi
from src.generate_from_ollama import get_summary
from src.generate_transcription import get_transcription
from src.write_to_file import save_summary_in_file
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
    summary = get_summary(transcription)
    save_summary_in_file(summary, fname)
    return JSONResponse({
        "summary": summary
        })
                
    
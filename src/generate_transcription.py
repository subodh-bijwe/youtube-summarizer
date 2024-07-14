from youtube_transcript_api import YouTubeTranscriptApi
from src.time_decorator import timeit

@timeit
def get_transcription(video_id):
    transcribed_data = YouTubeTranscriptApi.get_transcript(video_id)
    transcription = ""
    for t in transcribed_data:
        transcription += t["text"] + " "
    return transcription
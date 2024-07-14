import requests
import json
from src.time_decorator import timeit

@timeit
def get_summary(transcription):
    url = "http://localhost:11434/api/generate"
    prompt = f'''This is from a youtube video, please summarise the following text into nice bulleted points so it will be easy for 
    me to understand when I go back to those notes. No need to make the transcriptions crisp. Make it as explainable as possible. 
    Make sure the summary is in bullet points. and make it in markdown format.
    do not include anything like this 'Here is a summary of the text in markdown format, with headings and subpoints:', just return the summary
    Also give headings if new section begines, make sure there are subpoints wherever applicable.    
    The text is as follows: {transcription}'''
    # print(prompt)

    payload = json.dumps({
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    resp = response.json()["response"]
    return resp


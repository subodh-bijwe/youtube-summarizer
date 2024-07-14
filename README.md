# YouTube Video Summarizer using FastAPI

This application utilizes FastAPI to provide a summarization of YouTube video transcriptions using llama3 from ollama.

## Setup Instructions

1. **Install Dependencies**

    Ensure you have Python installed. Then install FastAPI and ollama:
    ```bash
    pip install -r requirements.txt
    ```

2. **Run ollama with llama3**

    Before running the FastAPI server, ensure ollama is installed and set up to run llama3. Follow ollama's documentation for installation and configuration instructions to start the llama3 service.
3. **Run the Application**

    Run the FastAPI server using Uvicorn:

    ```bash 
    uvicorn main:app --reload
    ```
    
    The API server will start running locally at `http://localhost:8000`.

4. **Usage**

- Access the FastAPI interactive documentation at `http://localhost:8000/docs`.
- Use the `/summarize` endpoint to submit a POST request with a JSON payload containing the YouTube video link.
- Example request:

  ```json
  {
    "link": "https://www.youtube.com/watch?v=<yourvideoid>"
  }
  ```

- The API will process the video transcription using llama3 from ollama and return a summarized text response.

5. **Endpoint**

- **POST /summarize**: Endpoint to summarize the transcription of a YouTube video.

6. **Dependencies**

- [FastAPI](https://fastapi.tiangolo.com/): FastAPI framework for building APIs with Python.
- [Uvicorn](https://www.uvicorn.org/): ASGI server for running FastAPI applications.
- [ollama](https://pypi.org/project/ollama/): Python package for working with llama3 transcription services.
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/): Python package which allows you to get the transcripts/subtitles for a given YouTube video.  

7. **Note**

- Make sure to have appropriate API keys or configurations set up for llama3 as per ollama's documentation.



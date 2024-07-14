import requests
from bs4 import BeautifulSoup
import re
from src.time_decorator import timeit

@timeit
def extract_video_id(url):
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/.*(?:\?|&)v=|youtu\.be/)([^&\n?#]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

@timeit
def get_video_title_from_link(video_id):
    if video_id:
        try:
            response = requests.get(f'https://www.youtube.com/watch?v={video_id}')
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('title').text
            return title.replace(' - YouTube', '')  # Clean up the title
        except Exception as e:
            print(f"Error fetching title: {e}")
            return None
    else:
        return None
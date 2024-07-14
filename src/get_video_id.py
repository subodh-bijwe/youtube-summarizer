import re
from src.time_decorator import timeit

@timeit
def get_id(video_link):
    # link will be in format https://www.youtube.com/watch?v=7n72snj0rqs
    # or this https://www.youtube.com/watch?v=Hxja4crycBg&list=PLsdq-3Z1EPT36NJXTutvKcreetuHCr9a-&index=19 if it is from a playlist

    match = re.search(r'v=([^&]+)', video_link)
    if match:
        return match.group(1)
    return None
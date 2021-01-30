from django.shortcuts import render
from googleapiclient.discovery import build
from config.settings import GOOGLE_API_KEY
import requests

from isodate import parse_duration

# Create your views here.
def youtube(request):

    videos = []

    if request.method == "POST":
        search_url = "https://www.googleapis.com/youtube/v3/search"
        video_url = "https://www.googleapis.com/youtube/v3/videos"

        query = request.POST.get("videos")

        search_params = {
            "part": "snippet",
            "q": query,
            "key": GOOGLE_API_KEY,
            "maxResults": 15,
            "type": "video",
        }

        video_ids = []

        r = requests.get(search_url, params=search_params)
        results = r.json()["items"]

        for result in results:
            video_ids.append(result["id"]["videoId"])
        
        video_params = {
            "key": GOOGLE_API_KEY,
            "part": "snippet, contentDetails",
            "id": ",".join(video_ids),
            "maxResults": 15,
        }

        r = requests.get(video_url, params=video_params)
        
        results = r.json()["items"]

        for result in results:
            title = result["snippet"]["title"]
            vid_id = result["id"]
            duration = int(parse_duration(result["contentDetails"]["duration"]).total_seconds() // 60)
            thumbnail = result["snippet"]["thumbnails"]["high"]["url"]

            video_data = {
                "title": title,
                "id": vid_id,
                "url": "https://www.youtube.com/watch?v={}".format(vid_id),
                "duration": duration,
                "thumbnail": thumbnail,
            }

            videos.append(video_data)
    
    # if request.method == 'POST':
    #     search_term = request.POST.get("youtube")
    #     print(search_term)

    context = {
        "videos": videos
    }
    return render(request, "youtube/youtube.html", context)

    
# GOOGLE_API_KEY=AIzaSyA1i-lhuJe7SUEbdo8Jd2-uWTvSpS5X6TA
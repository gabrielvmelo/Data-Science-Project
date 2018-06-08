from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import json
import pprint

DEVELOPER_KEY = "AIzaSyAtb1YJhXxXYq1nqkFft8TZvS9yVz253mQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results = 5, order = "relevance", token = None, location = None, location_radius = None):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q = q,
        type = "video",
        pageToken = token,
        order = order,
        part = "id, snippet",
        maxResults = max_results,
        location = location,
        locationRadius = location_radius
    ).execute()

    #print(search_response)

    return search_response

def youtube_stats(v):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    b = pprint.pformat(v)
    print(b)

    stats = youtube.videos().list(
        id = v['id']['videoId'],
        part = "statistics, snippet"
    ).execute()

    return stats

a = youtube_search("dua lipa")
test = a['items'][0]
#b = pprint.pformat(test)
video = youtube_stats(test)
c = pprint.pformat(video)
print(video)
e = json.dumps(video)
c = pprint.pformat(e)
print(c)
d = json.loads(e)
d = pprint.pformat(d)
print(d)
#print(b)
#print(a['items'])
print(type(a))
print(len(a))
    

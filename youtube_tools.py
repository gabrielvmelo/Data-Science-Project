from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import json
import pprint

DEVELOPER_KEY = "AIzaSyAtb1YJhXxXYq1nqkFft8TZvS9yVz253mQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results = 5, order = "relevance", token = None, location = None, location_radius = None, video_duration = 'any'):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q = q,
        type = "video",
        pageToken = token,
        order = order,
        part = "id, snippet",
        maxResults = max_results,
        location = location,
        locationRadius = location_radius,
        videoDuration = video_duration
    ).execute()

    #print(search_response)

    return search_response

def youtube_stats(v):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    b = pprint.pformat(v)
    #print(b)

    stats = youtube.videos().list(
        id = v['id']['videoId'],
        part = "statistics, snippet, contentDetails"
    ).execute()

    return stats

'''a = open("items.json").read()
b = json.loads(a)
print(type(b))
c = youtube_stats(b[0])
pprint.pprint(c)
b[0]['stats'] = c['items'][0]['statistics']
b[0]['tags'] = c['items'][0]['snippet']['tags']
b[0]['contentDetails'] = c['items'][0]['contentDetails']
b[0]['categoryId'] = c['items'][0]['snippet']['categoryId']
b[0]['publishedAt'] = c['items'][0]['snippet']['publishedAt']
pprint.pprint(b[0])'''
'''
for i in range(200):
    
    at = b[i+300]
    
    video = youtube_stats(at)
    print(type(video))
    
    items = video['items']
    #print(type(items))
    #print(len(video))
    #print(items)
    if items[0]['contentDetails']['definition'] != "hd":
        print(items[0]['contentDetails']['definition'])
    a += 1     
#pprint.pprint(c)'''

'''a = youtube_search("ed sheeran")
items = a['items']

arqout = open("out.json", 'w')
#arqout.write(json.dumps(items))

for item in items:
    arqout.write(json.dumps(item))
    arqout.write("\n")
'''
'''beauty = pprint.pformat(a)
print(beauty)
arqout = open("out.json", 'w')
arqout.write(json.dumps(a))

nexttoken = a["nextPageToken"]
b = youtube_search("ed sheeran", token=nexttoken)
beauty = pprint.pformat(b)
print(beauty)
arqout.write(json.dumps(b))'''
   

import json
import pprint

txt_in = open("ed_dataset.json").read()
videos = json.loads(txt_in)
arqout = open("out", 'w')
arqout.write("videoId\tchannelId\tdescription\tcategoryId\tdefinition\tduration\tlicensedContent\tpublishedAt\tcommentCount\tdislikeCount\tlikeCount\tviewCount\ttags\n")

pprint.pprint(videos[252])

for video in videos:
    info = []
    try:
        info.append(video['id']['videoId'])
        info.append(video['snippet']['channelId'])
        info.append(video['snippet']['description'])
        info.append(video['categoryId'])
        info.append(video['contentDetails']['definition'])
        info.append(video['contentDetails']['duration'])
        info.append(str(video['contentDetails']['licensedContent']))
        info.append(video['publishedAt'])
        info.append(video['stats']['commentCount'])
        info.append(video['stats']['dislikeCount'])
        info.append(video['stats']['likeCount'])
        info.append(video['stats']['viewCount'])
        info.append(json.dumps(video['tags']))
    except:
        continue

    for i in info:
        try:
            arqout.write(str(i) + "\t")
        except:
            arqout.write(json.dumps(i) + "\t")

    arqout.write("\n")